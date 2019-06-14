from rest_framework import views, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from api.budget.models import Budget, BudgetLine, Category, Role
from api.budget.serializers import BudgetSerializer, ProfileWithBudgetsSerializer, CreateBudgetLineSerializer, CategorySerializer, CreateRoleSerializer


class BudgetViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CreateRoleViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = CreateRoleSerializer

class BudgetLineViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = BudgetLine.objects.all()
    serializer_class = CreateBudgetLineSerializer

class ProfileWithBudgetsView(views.APIView):
    def get(self, request):
        serializer = ProfileWithBudgetsSerializer(self.request.user, context={'request': request})
        return Response(serializer.data)