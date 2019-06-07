# Generated by Django 2.2 on 2019-06-07 08:50

import api.budget.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0007_budgetline_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rel', models.CharField(choices=[(api.budget.models.RoleTypes('VIEWER'), 'VIEWER'), (api.budget.models.RoleTypes('ADMIN'), 'ADMIN')], max_length=8)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='budget.Budget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]