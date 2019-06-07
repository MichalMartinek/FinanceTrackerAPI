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
        fields = ('user', 'rel')

class BudgetLineSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = BudgetLine
        fields = ('description', 'amount', 'category',)

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    lines = BudgetLineSerializer(many=True, read_only=True)
    users = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ('id', 'name', 'date_created', 'date_updated', 'currency', 'lines', 'users')
        read_only_fields = ('id', 'date_created')

    @atomic
    def create(self, validated_data):
        usr = self.context['request'].user
        budget = Budget.objects.create(**validated_data)
        rel = RoleTypes.ADMIN.value
        print(rel)
        role = Role.objects.create(rel=rel, budget=budget, user=usr)
        return budget
