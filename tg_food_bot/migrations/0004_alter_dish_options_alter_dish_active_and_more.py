# Generated by Django 4.1.1 on 2022-09-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_food_bot', '0003_auto_20220921_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterField(
            model_name='dish',
            name='active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Показывать блюдо'),
        ),
        migrations.RemoveField(
            model_name='dish',
            name='categories',
        ),
        migrations.AlterField(
            model_name='dish',
            name='ingredients',
            field=models.TextField(blank=True, null=True, verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='recipe',
            field=models.TextField(blank=True, null=True, verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='dislikes',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='dislike_guests', to='tg_food_bot.dish', verbose_name='Не любимые рецепты'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='likes',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='like_guests', to='tg_food_bot.dish', verbose_name='Любимые рецепты'),
        ),
        migrations.RemoveField(
            model_name='guest',
            name='priority_categories',
        ),
        migrations.AddField(
            model_name='dish',
            name='categories',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='dishes', to='tg_food_bot.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='guest',
            name='priority_categories',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='guests', to='tg_food_bot.category', verbose_name='Любимые категория блюд'),
        ),
    ]