from django.contrib import admin
from api.budget.models import Budget, BudgetLine


# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    pass

class BudgetLineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Budget, BudgetAdmin)
admin.site.register(BudgetLine, BudgetLineAdmin)
