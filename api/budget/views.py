from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated 
from api.budget.models import Budget, Category
from api.budget.serializers import BudgetSerializer, CategorySerializer


class BudgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,) 
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
