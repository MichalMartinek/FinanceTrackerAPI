from django.urls import include, path
from rest_framework import routers
from api.core import views as viewsCore
from api.budget import views as viewsBudget
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', viewsCore.UserViewSet)
router.register(r'groups', viewsCore.GroupViewSet)
router.register(r'budgets', viewsBudget.BudgetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
