# Generated by Django 4.1.1 on 2022-09-27 19:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('title', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение')),
                ('ingredients', models.TextField(blank=True, null=True, verbose_name='Ингредиенты')),
                ('recipe', models.TextField(blank=True, null=True, verbose_name='Рецепт')),
                ('price', models.SmallIntegerField(blank=True, null=True, verbose_name='Цена порции')),
                ('active', models.BooleanField(db_index=True, default=True, verbose_name='Показывать блюдо')),
                ('categories', models.ManyToManyField(blank=True, db_index=True, related_name='dishes', to='tg_food_bot.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя')),
                ('telegram_id', models.IntegerField(unique=True, verbose_name='Телеграм ID')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region='RU', verbose_name='Номер телефона')),
                ('budget', models.IntegerField(blank=True, null=True, verbose_name='Бюджет')),
                ('dislikes', models.ManyToManyField(blank=True, db_index=True, related_name='dislike_guests', to='tg_food_bot.dish', verbose_name='Не любимые рецепты')),
                ('likes', models.ManyToManyField(blank=True, db_index=True, related_name='like_guests', to='tg_food_bot.dish', verbose_name='Любимые рецепты')),
                ('priority_categories', models.ManyToManyField(blank=True, db_index=True, related_name='guests', to='tg_food_bot.category', verbose_name='Любимые категория блюд')),
            ],
            options={
                'verbose_name': 'гостя',
                'verbose_name_plural': 'Гости',
            },
        ),
    ]
