from django.contrib.auth.models import User
from django.db import models
from enum import Enum

class Category(models.Model):
    code = models.CharField(max_length=128, primary_key=True,)

    def __str__(self):
        return self.code
    class Meta:
        verbose_name_plural = 'Categories'

class Budget(models.Model):
    name = models.CharField(max_length=256)
    currency = models.CharField(max_length=8)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class BudgetLine(models.Model):
    budget = models.ForeignKey(Budget, related_name='lines', on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    category = models.ForeignKey(Category, related_name='lines', null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.budget} - {self.id}'

class RoleTypes(Enum):
    VIEWER = "VIEWER"
    ADMIN = "ADMIN"

class Role(models.Model):
    budget = models.ForeignKey(Budget, related_name='users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='budgets', on_delete=models.CASCADE)
    rel = models.CharField(
      max_length=8,
      choices=tuple((i.value, i.name) for i in RoleTypes)  # Choices is a list of Tuple
    )

    def __str__(self):
        return f'{self.budget} <- {self.rel} -> {self.user}'