from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.budget.models import Budget, BudgetLine, Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class BudgetLineSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = BudgetLine
        fields = ('description', 'amount', 'category',)

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    lines = BudgetLineSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ('name', 'currency', 'lines',)
