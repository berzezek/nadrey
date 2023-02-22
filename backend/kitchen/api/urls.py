from django.urls import path

from .views import (
    ProductCategoryViewSet,
    ProductViewSet,
    ProductInStoreViewSet,
    ProductForRecipeViewSet,
    CategoryRecipeViewSet,
    RecipeViewSet,
    ClientViewSet,
    OrderViewSet,
    CardViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product-category', ProductCategoryViewSet)
router.register('product', ProductViewSet)
router.register('product-in-store', ProductInStoreViewSet)
router.register('product-for-recipe', ProductForRecipeViewSet)
router.register('category-recipe', CategoryRecipeViewSet)
router.register('recipe', RecipeViewSet)
router.register('client', ClientViewSet)
router.register('order', OrderViewSet)
router.register('card', CardViewSet)

urlpatterns = [
]

urlpatterns += router.urls
