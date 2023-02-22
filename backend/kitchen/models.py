from django.db import models
from django.utils.datetime_safe import datetime


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категорию продукта'
        verbose_name_plural = 'Категории продуктов'

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    UNIT_CHOICES = (
        ('kg', 'кг'),
        ('gr', 'гр'),
        ('l', 'л'),
        ('ml', 'мл'),
        ('pcs', 'шт'),
    )

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='kg', verbose_name='Единица измерения')
    calories = models.IntegerField(null=True, blank=True, verbose_name='Калорийность ккал')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Категория')

    def __str__(self):
        return f'{self.name} ({self.unit})'


class ProductInStore(models.Model):
    class Meta:
        verbose_name = 'Продукт на складе'
        verbose_name_plural = 'Продукты на складе'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True, verbose_name='Срок годности')
    quantity = models.FloatField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Закупочная цена')

    def __str__(self):
        return f'{self.product.name} - {self.quantity}/{self.product.unit}'


class Store(models.Model):
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class StoreTransaction(models.Model):
    TRANSACTION_TYPE = (
        ('in', 'Приход'),
        ('out', 'Расход'),
        ('trash', 'Списание')
    )

    class Meta:
        verbose_name = 'Транзакцию'
        verbose_name_plural = 'Транзакции'

    date = models.DateField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='Склад')
    product = models.ForeignKey(ProductInStore, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.FloatField(verbose_name='Количество')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    def __str__(self):
        return f'{self.store.name} - {self.product.name} - {self.quantity}/{self.product.unit}'


class ProductForRecipe(models.Model):
    class Meta:
        verbose_name = 'Продукт для рецепта'
        verbose_name_plural = 'Продукты для рецепта'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    quantity = models.FloatField(verbose_name='Количество')

    def __str__(self):
        return f'{self.product.name} - {self.quantity}/{self.product.unit}'


class CategoryRecipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images', default='images/default.png', verbose_name='Изображение')
    products = models.ManyToManyField(ProductForRecipe, verbose_name='Продукты для рецепта')
    category = models.ForeignKey(CategoryRecipe, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Категория')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    phone = models.CharField(max_length=20, verbose_name='Контакты')
    email = models.EmailField(null=True, blank=True, verbose_name='Почта')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    quantity = models.IntegerField(verbose_name='Количество')
    date = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнен')

    def __str__(self):
        return self.recipe.name


class Card(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    date_created = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    order = models.ManyToManyField(Order, verbose_name='Заказ')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')

    def __str__(self):
        return self.name
