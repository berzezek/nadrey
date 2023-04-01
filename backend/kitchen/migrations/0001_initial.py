# Generated by Django 4.1.7 on 2023-04-01 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('phone', models.CharField(max_length=20, verbose_name='Контакты')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('quantity', models.FloatField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Продукт для рецепта',
                'verbose_name_plural': 'Продукты для рецепта',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('unit', models.CharField(choices=[('kg', 'кг'), ('gr', 'гр'), ('l', 'л'), ('ml', 'мл'), ('pcs', 'шт')], default='kg', max_length=15, verbose_name='Единица измерения')),
                ('weight', models.FloatField(default=1, verbose_name='Удельный вес')),
                ('calories', models.IntegerField(blank=True, default=0, null=True, verbose_name='Калорийность ккал')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категорию продукта',
                'verbose_name_plural': 'Категории продуктов',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images', verbose_name='Изображение')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Вес')),
                ('price', models.FloatField(blank=True, default=0, null=True, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.categoryrecipe', verbose_name='Категория')),
                ('products', models.ManyToManyField(blank=True, to='kitchen.ingredients', verbose_name='Продукты для рецепта')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='ProductInStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='Срок годности')),
                ('quantity', models.FloatField(verbose_name='Количество')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Закупочная цена')),
                ('transaction_type', models.CharField(blank=True, choices=[('in', 'Приход'), ('out', 'Расход'), ('move', 'Перемещение'), ('write_off', 'Списание'), ('data_off', 'Списание по дате')], default='in', max_length=15, null=True, verbose_name='Тип операции')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.product', verbose_name='Продукт')),
                ('store', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kitchen.store', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Продукт на складе',
                'verbose_name_plural': 'Продукты на складе',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kitchen.productcategory', verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('quantity', models.FloatField(verbose_name='Количество')),
                ('date', models.DateField(auto_now_add=True)),
                ('date_completed', models.DateField(blank=True, null=True, verbose_name='Дата выполнения')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Выполнен')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.recipe', verbose_name='Рецепт')),
            ],
        ),
        migrations.AddField(
            model_name='ingredients',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.product', verbose_name='Продукт'),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.client', verbose_name='Клиент')),
                ('order', models.ManyToManyField(blank=True, to='kitchen.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]
