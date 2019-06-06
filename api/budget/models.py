from django.db import models

class Budget(models.Model):
    name = models.CharField(max_length=256)

class BudgetLine(models.Model):
    budget = models.ForeignKey(Budget, related_name='lines', on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    amount = models.IntegerField()