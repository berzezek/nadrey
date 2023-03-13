from rest_framework.viewsets import ModelViewSet

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


# noinspection DuplicatedCode
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
