from rest_framework.fields import IntegerField
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

    def get_category_name(self, obj):
        return obj.category.name

    def get_unit_russian(self, obj):
        # case
        if obj.unit == 'kg':
            return 'кг'
        elif obj.unit == 'gr':
            return 'гр'
        elif obj.unit == 'l':
            return 'л'
        elif obj.unit == 'ml':
            return 'мл'
        elif obj.unit == 'pcs':
            return 'шт'

    category_name = SerializerMethodField(
        method_name='get_category_name',
        read_only=True,
    )

    unit_russian = SerializerMethodField(
        method_name='get_unit_russian',
        read_only=True,
    )

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'category_name',
            'unit',
            'unit_russian',
            'category',
            'weight',
            'calories',
        )


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductInStoreSerializer(ModelSerializer):
    def get_product_unit_russian(self, obj):
        # case
        if obj.product.unit == 'kg':
            return 'кг'
        elif obj.product.unit == 'gr':
            return 'гр'
        elif obj.product.unit == 'l':
            return 'л'
        elif obj.product.unit == 'ml':
            return 'мл'
        elif obj.product.unit == 'pcs':
            return 'шт'

    def get_transaction_type_russian(self, obj):
        if obj.transaction_type == 'in':
            return 'Приход'
        elif obj.transaction_type == 'out':
            return 'Расход'
        elif obj.transaction_type == 'write_off':
            return 'Списание'

    product_name = CharField(source='product.name', read_only=True)
    product_unit = SerializerMethodField(
        method_name='get_product_unit_russian',
        read_only=True
    )
    transaction_type_russian = SerializerMethodField(
        method_name='get_transaction_type_russian',
        read_only=True
    )

    class Meta:
        model = ProductInStore
        fields = (
            'id',
            'product',
            'product_name',
            'product_unit',
            'quantity',
            'transaction_type',
            'transaction_type_russian',
            'price',
            'expiration_date',
            'description',
            'store',
        )
        ordering = [ 'product' ]


class IngredientsSerializer(ModelSerializer):
    product_name = CharField(source='product.name', read_only=True)
    product_unit = CharField(source='product.unit', read_only=True)
    last_price = SerializerMethodField(read_only=True)
    max_price = SerializerMethodField(read_only=True)
    average_price = SerializerMethodField(read_only=True)
    ingredient_weight = SerializerMethodField(read_only=True)

    def get_ingredient_weight(self, obj):
        if obj.product.unit == 'gr':
            return obj.quantity / 1000
        elif obj.product.unit == 'l':
            return obj.quantity * obj.product.weight
        elif obj.product.unit == 'ml':
            return obj.quantity * obj.product.weight / 1000
        elif obj.product.unit == 'pcs':
            return obj.quantity * obj.product.weight
        else:
            return obj.quantity

    def get_max_price(self, obj):
        max_price = (ProductInStore.objects.filter(product=obj.product_id, price__isnull=False)
        .aggregate(Max('price'))['price__max' ])
        return max_price


    def get_average_price(self, obj):
        average_price = (ProductInStore.objects.filter(product=obj.product_id, price__isnull=False)
        .aggregate(Avg('price'))['price__avg' ])
        return round(average_price)

    def get_last_price(self, obj):
        return ProductInStore.objects.filter(product=obj.product_id, price__isnull=False).last().price

    class Meta:
        model = Ingredients
        fields = (
            'id',
            'product',
            'quantity',
            'description',
            'product_name',
            'product_unit',
            'last_price',
            'average_price',
            'max_price',
            'ingredient_weight'
        )


class CategoryRecipeSerializer(ModelSerializer):
    class Meta:
        model = CategoryRecipe
        fields = '__all__'


class RecipeSerializer(ModelSerializer):
    products = IngredientsSerializer(many=True, read_only=True)
    category_name = CharField(source='category.name', read_only=True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'category',
            'category_name',
            'products',
            'image',
            'weight',
            'price',
        )


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    recipe_name = CharField(source='recipe.name', read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'recipe',
            'recipe_name',
            'quantity',
            'is_completed',
        )


class CardSerializer(ModelSerializer):

    def get_total_price(self, obj):
        orders = Order.objects.filter(card=obj.id)
        total_price = 0
        for order in orders:
            total_price += order.recipe.price * order.quantity
        return total_price
    def get_order(self, obj):
        orders = Order.objects.filter(card=obj.id)
        return OrderSerializer(orders, many=True).data

    card_client = CharField(source='client.name', read_only=True)
    get_orders = SerializerMethodField(
        method_name='get_order',
        read_only=True,
    )
    total_price = SerializerMethodField(read_only=True)

    class Meta:
        model = Card
        fields = (
            'id',
            'client',
            'card_client',
            'order',
            'get_orders',
            'is_paid',
            'date_created',
            'total_price',
        )
