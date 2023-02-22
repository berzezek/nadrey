from django.db.models import F

from ..models import (
    ProductCategory,
    Product,
    ProductInStore,
    ProductForRecipe,
    CategoryRecipe,
    Recipe,
    Client,
    Order,
    Card,
)

from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductInStoreSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductInStore
        fields = '__all__'


class ProductForRecipeSerializer(ModelSerializer):
    class Meta:
        model = ProductForRecipe
        fields = '__all__'


class CategoryRecipeSerializer(ModelSerializer):
    class Meta:
        model = CategoryRecipe
        fields = '__all__'


class RecipeSerializer(ModelSerializer):

    def get_total_price(self, obj):
        total = 0
        for product in obj.products.all():
            print(product.__dict__)
            try:
                price = ProductInStore.objects.get(product=product.product_id).price
                total += price
            except ProductInStore.DoesNotExist:
                return f'Нет актуальных цен на продукты: {product.product}'

        return total

    def get_total_calories(self, obj):
        total = 0
        for product in obj.products.all():
            try:
                total += product.product.calories
            except AttributeError:
                return f'Неизвестны калории: {product.product}'
        return total

    total_calories = SerializerMethodField(
        method_name='get_total_calories',
        read_only=True,
    )

    total_price = SerializerMethodField(
        method_name='get_total_price',
        read_only=True,
    )

    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'image',
            'products',
            'category',
            'total_calories',
            'total_price',
        )


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    def get_order_price(self, obj):
        total = 0
        for order in obj.recipe.products.all():
            try:
                price = ProductInStore.objects.get(product=order.product_id).price
                total += price * obj.quantity
            except ProductInStore.DoesNotExist:
                return f'Нет актуальных цен на продукты: {order.product}'
        return total

    order_price = SerializerMethodField(
        method_name='get_order_price',
        read_only=True,
    )

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        for product in order.recipe.products.all():
            product_in_store = ProductInStore.objects.get(product=product.product_id)
            product_in_store.quantity = F('quantity') - order.quantity * order.recipe.products.get(
                product=product.product_id).quantity
            product_in_store.save()
        return order

    class Meta:
        model = Order
        fields = (
            'id',
            'recipe',
            'description',
            'quantity',
            'date',
            'date_completed',
            'is_completed',
            'order_price',
        )


class CardSerializer(ModelSerializer):

    def get_card_price(self, obj):
        total = 0
        for card in obj.order.all():
            for product in Recipe.objects.get(id=card.recipe_id).products.all():
                try:
                    price = ProductInStore.objects.get(product=product.product_id).price
                    total += price * card.quantity
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
