from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api.core import views as viewsCore
from api.budget import views as viewsBudget

router = routers.DefaultRouter()
router.register(r'users', viewsCore.UserViewSet)
router.register(r'budgets', viewsBudget.BudgetViewSet)
router.register(r'categories', viewsBudget.CategoryViewSet)
router.register(r'roles', viewsBudget.CreateRoleViewSet)
router.register(r'lines', viewsBudget.BudgetLineViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^profile/$', viewsBudget.ProfileWithBudgetsView.as_view(), name='profile-budgets'),
    url(r'^search-user/(?P<query>.+)$', viewsCore.SearchUserView.as_view(), name='search-user'),
    path('', include(router.urls)),
    path('api-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
]
