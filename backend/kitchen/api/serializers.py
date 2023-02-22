from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

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
    # def get_quantity_for_product_in_store(self, obj):
    #     quantity = 0
    #     for product in ProductInStore.objects.filter(product=obj.product):
    #         if product.transaction_type == 'in':
    #             quantity += product.quantity
    #         else:
    #             quantity -= product.quantity
    #     return quantity
    #
    # get_quantity = SerializerMethodField(
    #     method_name='get_quantity_for_product_in_store',
    #     read_only=True,
    # )

    class Meta:
        model = ProductInStore
        fields = (
            'id',
            'product',
            'product_name',
            'transaction_type',
            'quantity',
            # 'get_quantity',
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

    def get_total_price(self, obj):
        total = 0
        for product in obj.products.all():
            try:
                price = ProductInStore.objects.filter(product=product.product_id).last().price * product.quantity
                total += price
            except AttributeError:
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

    def get_total_product_weight(self, obj):
        total = 0
        for product in obj.products.all():
            try:
                total += product.quantity
            except AttributeError:
                return f'Неизвестный вес: {product.product}'
        return total

    total_calories = SerializerMethodField(
        method_name='get_total_calories',
        read_only=True,
    )

    total_price = SerializerMethodField(
        method_name='get_total_price',
        read_only=True,
    )

    product_weight = SerializerMethodField(
        method_name='get_total_product_weight',
        read_only=True,
    )

    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'image',
            'price',
            'products',
            'category',
            'total_calories',
            'total_price',
            'weight',
            'product_weight',
        )


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    def get_order_price(self, obj):
        total = 0
        for product in obj.recipe.products.all():
            try:
                price = ProductInStore.objects.filter(product=product.product_id, price__isnull=False).last().price
                ingradient_quantity = Ingredients.objects.get(product=product.product_id).quantity
                total += price * ingradient_quantity * obj.quantity
            except ProductInStore.DoesNotExist:
                return f'Нет актуальных цен на продукты: {product.product}'
        return total

    order_price = SerializerMethodField(
        method_name='get_order_price',
        read_only=True,
    )

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        for product in order.recipe.products.all():
            ingradient_quantity = Ingredients.objects.get(product=product.product_id).quantity
            product_out_store = ProductInStore(product=product.product, transaction_type='out',
                                               quantity=ingradient_quantity)
            product_out_store.save()
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
