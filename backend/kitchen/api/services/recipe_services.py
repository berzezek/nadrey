from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ...models import Recipe

from ..serializers import RecipeSerializer
from ...models import ProductInStore

def get_ingredients_price(items, price_type=None):
    total_price = 0
    for item in items:
        try:
            total_price += item[price_type] * item['quantity']
        except ProductInStore.DoesNotExist:
            pass
    return round(total_price)

def get_ingredients_weight(ingredients):
    total_weight = 0
    for ingredient in ingredients:
        try:
            total_weight += ingredient['ingredient_weight']
        except ProductInStore.DoesNotExist:
            pass
    return round(total_weight, 2)


class RecipeAPIView(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        for recipe in serializer.data:
            recipe['total_last_price'] = get_ingredients_price(recipe['products'], 'last_price')
            recipe['total_average_price'] = get_ingredients_price(recipe['products'], 'average_price')
            recipe['total_max_price'] = get_ingredients_price(recipe['products'], 'max_price')
            recipe['total_weight'] = get_ingredients_weight(recipe['products'])
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data[ 'total_last_price' ] = get_ingredients_price(data[ 'products' ], 'last_price')
        data[ 'total_average_price' ] = get_ingredients_price(data[ 'products' ], 'average_price')
        data[ 'total_max_price' ] = get_ingredients_price(data[ 'products' ], 'max_price')
        data[ 'total_weight' ] = get_ingredients_weight(data[ 'products' ])
        return Response(data)
