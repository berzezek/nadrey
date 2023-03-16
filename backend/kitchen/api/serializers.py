from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from django.db import models
from django.db.models import Max, Avg

from ..models import (
    ProductCategory,
    Product,
    Store,
    ProductInStore,
    Ingredients,
    CategoryRecipe,
    Recipe,
    Client,
    Order,
    Card,
)


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductInStoreSerializer(ModelSerializer):
    product_name = CharField(source='product.name', read_only=True)
    product_unit = CharField(source='product.unit', read_only=True)

    class Meta:
        model = ProductInStore
        fields = (
            'id',
            'product',
            'product_name',
            'product_unit',
            'quantity',
            'transaction_type',
            'price',
            'expiration_date',
            'description',
            'store',
        )
        ordering = ['product']


class IngredientsSerializer(ModelSerializer):
    class Meta:
        model = Ingredients
        fields = (
            'id',
            'product',
            'quantity',
            'description',
        )


class CategoryRecipeSerializer(ModelSerializer):
    class Meta:
        model = CategoryRecipe
        fields = '__all__'


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CardSerializer(ModelSerializer):
    card_client = CharField(source='client.name', read_only=True)

    # def get_card_price(self, obj):
    #     total = 0
    #     for order in obj.order.all():
    #         for product in order.recipe.products.all():
    #             try:
    #                 price = ProductInStore.objects.filter(product=product.product_id, price__isnull=False).last().price
    #                 ingradient_quantity = Ingredients.objects.get(product=product.product_id).quantity
    #                 total += price * ingradient_quantity * order.quantity
    #             except ProductInStore.DoesNotExist:
    #                 return f'Нет актуальных цен на продукты: {product.product}'
    #     return total
    #
    # card_price = SerializerMethodField(
    #     method_name='get_card_price',
    #     read_only=True,
    # )

    class Meta:
        model = Card
        fields = (
            'id',
            'client',
            'card_client',
            'order',
            'is_paid',
        )
