from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import (
    ProductCategoryViewSet,
    ProductViewSet,
    ProductInStoreViewSet,
    ProductForRecipeViewSet,
    CategoryRecipeViewSet,
    RecipeViewSet,
    ClientViewSet,
    OrderViewSet,
    CardViewSet,
    schema_view,
)

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
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls
