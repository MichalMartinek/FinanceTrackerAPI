from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.budget.models import Budget

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Budget
        fields = ('name',)