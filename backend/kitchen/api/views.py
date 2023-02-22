from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.viewsets import ModelViewSet
from django.db.models import Case, When, Sum, F, FloatField

# from rest_framework.response import Response
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


# class GroupedProductInStoreViewSet(ModelViewSet):
#     serializer_class = ProductServiceSerializer
#     queryset = ProductInStore.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


schema_view = get_schema_view(
    openapi.Info(
        title="nadrey API",
        default_version='v1',
        description="Test description",
        terms_of_service="http://localhost/api/v1/",
        contact=openapi.Contact(email="wknduz@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
