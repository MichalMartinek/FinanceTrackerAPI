from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.budget.models import Budget, BudgetLine

class BudgetLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BudgetLine
        fields = ('description', 'amount')

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    lines = BudgetLineSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ('name','lines')
