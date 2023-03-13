from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum, Case, When, F, FloatField

from rest_framework.response import Response
# from .services.product_service import ProductServiceSerializer

from .serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    StoreSerializer,
    ProductInStoreSerializer,
    IngredientsSerializer,
    CategoryRecipeSerializer,
    RecipeSerializer,
    ClientSerializer,
    OrderSerializer,
    CardSerializer,
)
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



class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductInStoreViewSet(ModelViewSet):
    queryset = ProductInStore.objects.all()
    serializer_class = ProductInStoreSerializer


class IngredientsViewSet(ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class CategoryRecipeViewSet(ModelViewSet):
    queryset = CategoryRecipe.objects.all()
    serializer_class = CategoryRecipeSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# class StockBalanceAPIView(APIView):
#     def get(self, request, format=None):
#         # Получаем остатки продуктов на складе, сгруппированные по продукту и складу
#         product_stocks = ProductInStore.objects.values(
#             'product__name', 'store__name'
#         ).annotate(
#             total_quantity=Sum(
#                 Case(
#                     When(price=None, then=F('quantity') * -1),
#                     default=F('quantity'),
#                     output_field=FloatField()
#                 )
#             )
#         )
#
#         # Формируем сводную таблицу из полученных данных
#         stock_balance = {}
#         for ps in product_stocks:
#             product_name = ps['product__name']
#             store_name = ps['store__name']
#             total_quantity = ps['total_quantity']
#
#             if product_name not in stock_balance:
#                 stock_balance[product_name] = {}
#
#             stock_balance[product_name][store_name] = total_quantity
#
#         # Преобразуем данные в нужный формат для вывода
#         balance_data = []
#         for product_name, stores in stock_balance.items():
#             for store_name, total_quantity in stores.items():
#                 balance_data.append({
#                     'product': product_name,
#                     'store': store_name,
#                     'quantity': total_quantity,
#                 })
#
#         # Возвращаем сводную таблицу в виде JSON-ответа
#         return Response(balance_data)


