from django.contrib import admin
from api.budget.models import Budget, BudgetLine, Category, Role


# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    pass

class BudgetLineAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class RoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Budget, BudgetAdmin)
admin.site.register(BudgetLine, BudgetLineAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Category, CategoryAdmin)
