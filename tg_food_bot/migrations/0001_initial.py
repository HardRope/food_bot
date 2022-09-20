# Generated by Django 4.1.1 on 2022-09-20 20:01

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('image', models.ImageField(null=True, upload_to='images', verbose_name='Изображение')),
                ('category', models.CharField(blank=True, choices=[('VG', 'Вегатарианские блюда'), ('FH', 'Рыбные блюда'), ('SL', 'Салаты'), ('GL', 'Блюда без глютена')], db_index=True, max_length=2, primary_key=True, serialize=False, verbose_name='Категория')),
                ('ingredients', models.TextField(verbose_name='Ингредиенты')),
                ('recipe', models.TextField(verbose_name='Рецепт приготовления')),
                ('active', models.BooleanField(db_index=True, default=True, null=True, verbose_name='Показать гостям')),
            ],
            options={
                'verbose_name': 'рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(blank=True, unique=True, verbose_name='Телеграм ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region='RU', verbose_name='Номер телефона')),
                ('dislikes', models.ManyToManyField(blank=True, db_index=True, related_name='dislike_guests', to='tg_food_bot.dish', verbose_name='Не любимые рецепты')),
                ('likes', models.ManyToManyField(blank=True, db_index=True, related_name='like_guests', to='tg_food_bot.dish', verbose_name='Любимые рецепты')),
                ('priority_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guests', to='tg_food_bot.dish', verbose_name='Любимая категория блюд')),
            ],
            options={
                'verbose_name': 'гостя',
                'verbose_name_plural': 'Гости',
            },
        ),
    ]
