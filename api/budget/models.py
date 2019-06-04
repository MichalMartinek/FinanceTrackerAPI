from django.db import models

class Budget(models.Model):
    name = models.CharField(max_length=256)
