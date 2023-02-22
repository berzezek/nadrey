from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

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

from .serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    ProductInStoreSerializer,
    ProductForRecipeSerializer,
    CategoryRecipeSerializer,
    RecipeSerializer,
    ClientSerializer,
    OrderSerializer,
    CardSerializer,
)
from rest_framework.viewsets import ModelViewSet


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInStoreViewSet(ModelViewSet):
    queryset = ProductInStore.objects.all()
    serializer_class = ProductInStoreSerializer


class ProductForRecipeViewSet(ModelViewSet):
    queryset = ProductForRecipe.objects.all()
    serializer_class = ProductForRecipeSerializer


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
