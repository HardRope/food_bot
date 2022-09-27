# Generated by Django 4.1.1 on 2022-09-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_food_bot', '0008_auto_20220927_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='price',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='price_currency',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='budget_currency',
        ),
        migrations.AlterField(
            model_name='guest',
            name='budget',
            field=models.IntegerField(blank=True, null=True, verbose_name='Бюджет'),
        ),
    ]
