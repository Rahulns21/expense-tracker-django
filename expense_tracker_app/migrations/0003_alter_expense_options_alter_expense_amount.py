# Generated by Django 5.0.2 on 2024-02-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker_app', '0002_alter_expense_options_expense_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name_plural': 'Expenses'},
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
