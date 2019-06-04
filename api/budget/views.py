from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from api.budget.models import Budget
from api.budget.serializers import BudgetSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,) 
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
