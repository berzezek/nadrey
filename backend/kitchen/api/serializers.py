from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from django.db.models import Max

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

    @staticmethod
    def get_products(obj):
        products = []
        for i in obj.products.all():
            products.append({
                'id': i.product.id,
                'name': i.product.name,
                'quantity': i.quantity,
                'unit': i.product.unit,
            })
        return products

    @staticmethod
    def get_category_name(obj):
        return obj.category.name

    @staticmethod
    def get_total_weight(obj):
        total_weight = 0
        for i in obj.products.all():
            try:
                product = Product.objects.get(id=i.product_id)
                if product.unit == 'кг':
                    specific_gravity = 1
                elif product.unit == 'г':
                    specific_gravity = 1 / 1000
                else:
                    specific_gravity = product.weight
                weight = i.quantity * specific_gravity
            except Exception as e:
                print(e)
                weight = 0
            total_weight += weight
        return total_weight

    @staticmethod
    def get_total_price(obj):
        total_price = 0
        for i in obj.products.all():
            try:
                price = ProductInStore.objects.filter(
                    product=i.product_id,
                    price__isnull=False
                ).aggregate(Max('price'))['price__max'] * i.quantity
            except Exception as e:
                print(e)
                price = 0
            total_price += price
        return total_price

    total_price = SerializerMethodField('get_total_price', read_only=True)
    total_weight = SerializerMethodField('get_total_weight', read_only=True)
    get_recipe_products = SerializerMethodField('get_products', read_only=True)
    get_category = SerializerMethodField('get_category_name', read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'image',
            'price',
            'total_price',
            'products',
            'get_recipe_products',
            'category',
            'get_category',
            'weight',
            'total_weight',
        )


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    # def get_order_price(self, obj):
    #     total = 0
    #     for product in obj.recipe.products.all():
    #         try:
    #             price = ProductInStore.objects.filter(product=product.product_id, price__isnull=False).last().price
    #             ingradient_quantity = Ingredients.objects.get(product=product.product_id).quantity
    #             total += price * ingradient_quantity * obj.quantity
    #         except ProductInStore.DoesNotExist:
    #             return f'Нет актуальных цен на продукты: {product.product}'
    #     return total
    #
    # order_price = SerializerMethodField(
    #     method_name='get_order_price',
    #     read_only=True,
    # )
    #
    # def create(self, validated_data):
    #     order = Order.objects.create(**validated_data)
    #     for product in order.recipe.products.all():
    #         ingradient_quantity = Ingredients.objects.get(product=product.product_id).quantity
    #         product_out_store = ProductInStore(product=product.product, transaction_type='out',
    #                                            quantity=ingradient_quantity)
    #         product_out_store.save()
    #     return order

    class Meta:
        model = Order
        fields = '__all__'
        # fields = (
        #     'id',
        #     'cooking-recipe',
        #     'description',
        #     'quantity',
        #     'date',
        #     'date_completed',
        #     'is_completed',
        #     'order_price',
        # )


class CardSerializer(ModelSerializer):

    def get_card_price(self, obj):
        total = 0
        for order in obj.order.all():
            for product in order.recipe.products.all():
                try:
                    price = ProductInStore.objects.filter(product=product.product_id, price__isnull=False).last().price
                    ingradient_quantity = Ingredients.objects.get(product=product.product_id).quantity
                    total += price * ingradient_quantity * order.quantity
                except ProductInStore.DoesNotExist:
                    return f'Нет актуальных цен на продукты: {product.product}'
        return total

    card_price = SerializerMethodField(
        method_name='get_card_price',
        read_only=True,
    )

    class Meta:
        model = Card
        fields = (
            'id',
            'date_created',
            'description',
            'order',
            'client',
            'is_paid',
            'card_price',
        )
