from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from .views import (
    ProductCategoryViewSet,
    ProductViewSet,
    StoreViewSet,
    ProductInStoreViewSet,
    IngredientsViewSet,
    CategoryRecipeViewSet,
    RecipeViewSet,
    ClientViewSet,
    OrderViewSet,
    CardViewSet,
)

from .services.api_doc import schema_view
from .services.stock_balance import StockBalanceAPIView

router = DefaultRouter()
router.register('product-category', ProductCategoryViewSet)
router.register('product', ProductViewSet)
router.register('stock', StoreViewSet)
router.register('product-in-stock', ProductInStoreViewSet)
router.register('ingredients', IngredientsViewSet)
router.register('category-cooking-recipe', CategoryRecipeViewSet)
router.register('cooking-recipe', RecipeViewSet)
router.register('client', ClientViewSet)
router.register('order', OrderViewSet)
router.register('card', CardViewSet)
# router.register('grouped-product-in-stock', GroupedProductInStoreViewSet)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('stock-balance/', StockBalanceAPIView.as_view(), name='stock_balance'),
]

urlpatterns += router.urls
