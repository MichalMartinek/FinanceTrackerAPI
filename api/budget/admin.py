from django.contrib import admin
from api.budget.models import Budget


# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Budget, BudgetAdmin)
