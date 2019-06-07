from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api.core import views as viewsCore
from api.budget import views as viewsBudget

router = routers.DefaultRouter()
router.register(r'users', viewsCore.UserViewSet)
router.register(r'groups', viewsCore.GroupViewSet)
router.register(r'budgets', viewsBudget.BudgetViewSet)
router.register(r'categories', viewsBudget.CategoryViewSet)
router.register(r'roles', viewsBudget.CreateRoleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
]
