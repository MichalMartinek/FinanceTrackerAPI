from django.contrib.auth.models import User, Group
from django.db.transaction import atomic
from rest_framework import serializers
from api.budget.models import Budget, BudgetLine, Category, Role, RoleTypes
from api.core.serializers import UserSerializer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('code',)

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Role
        fields = ('user', 'rel', 'id')

class BudgetLineSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = BudgetLine
        fields = ('description', 'amount', 'category', 'date_created', 'id')
        read_only_fields = ('id', 'date_created')

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    lines = BudgetLineSerializer(many=True, read_only=True)
    users = RoleSerializer(many=True, read_only=True)
    modified_by = UserSerializer(read_only=True)

    class Meta:
        model = Budget
        fields = ('id', 'name', 'date_created', 'date_updated', 'currency', 'modified_by', 'lines', 'users')
        read_only_fields = ('id', 'date_created', 'date_updated')

    @atomic
    def create(self, validated_data):
        print(self.context['request'].user.budgets)
        usr = self.context['request'].user
        validated_data["modified_by"] = usr
        budget = Budget.objects.create(**validated_data)
        rel = RoleTypes.ADMIN.value
        print(rel)
        role = Role.objects.create(rel=rel, budget=budget, user=usr)
        return budget

    @atomic
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.currency = validated_data['currency']
        instance.modified_by = self.context['request'].user
        instance.save()
        return instance

class BudgetWithRoleSerializer(serializers.Serializer):
    budget = BudgetSerializer(read_only=True)
    rel = serializers.CharField(read_only=True)

    class Meta:
        model = Role
        fields = ('budget', 'rel')

class ProfileWithBudgetsSerializer(serializers.HyperlinkedModelSerializer):
    budgets = BudgetWithRoleSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'budgets')

class CreateRoleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    budget_id = serializers.IntegerField()
    rel = serializers.ChoiceField(choices=[item.value for item in RoleTypes], default=RoleTypes.ADMIN.value)

    class Meta:
        model = Role
        fields = ('user', 'rel', 'budget')
    @atomic
    def create(self, validated_data):
        print(validated_data)
        instance = Role(rel=validated_data['rel'])
        instance.user_id = validated_data['user_id']
        instance.budget_id = validated_data['budget_id']
        instance.save()
        return instance

    @atomic
    def update(self, instance, validated_data):
        instance.rel = validated_data['rel']
        instance.user_id = validated_data['user_id']
        instance.budget_id = validated_data['budget_id']
        instance.save()
        return instance


class CreateBudgetLineSerializer(serializers.Serializer):
    budget_id = serializers.IntegerField()
    category_id = serializers.CharField()
    description = serializers.CharField(max_length=256)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = BudgetLine
        fields = ('description', 'amount', 'category', 'budget')
    @atomic
    def create(self, validated_data):
        print(validated_data)
        instance = BudgetLine(description=validated_data['description'], amount=validated_data['amount'])
        instance.category_id = validated_data['category_id']
        instance.budget_id = validated_data['budget_id']
        instance.save()
        return instance

    @atomic
    def update(self, instance, validated_data):
        instance.description = validated_data['description']
        instance.amount = validated_data['amount']
        instance.category_id = validated_data['category_id']
        instance.budget_id = validated_data['budget_id']
        instance.save()
        return instance