from rest_framework import generics
from rest_framework.response import Response
from ...models import Recipe, Ingredients, CategoryRecipe
from .last_price import get_max_average_price

from ..serializers import RecipeSerializer


def update_serialize_data(data):
    category = CategoryRecipe.objects.get(id=data['category'])
    products = []
    unit_weight = 1
    total_product_weight = 0
    total_max_price = 0
    total_average_price = 0
    for pk in data['products']:
        try:
            ingredient = Ingredients.objects.get(id=pk)

            balanced_product = get_max_average_price()

            if ingredient.product.unit == 'gr':
                unit_weight = 1 / 1000 * ingredient.quantity
            elif ingredient.product.unit == 'kg':
                unit_weight = ingredient.quantity
            if ingredient.product.weight:
                unit_weight = ingredient.product.weight * ingredient.quantity

            average_price = balanced_product[0]['average_last_3_prices']
            max_price = balanced_product[0]['max_last_3_prices']

            if average_price != 'Нет цены':
                average_price = average_price * unit_weight

            if max_price != 'Нет цены':
                max_price = max_price * unit_weight

            products.append({
                'id': pk,
                'name': ingredient.product.name,
                'quantity': ingredient.quantity,
                'unit': ingredient.product.unit,
                'unit_weight': unit_weight,
                'average_price': average_price,
                'max_price': max_price,
            })
            total_product_weight += unit_weight if unit_weight != 'Нет цены' else 0
            total_max_price += max_price if max_price != 'Нет цены' else 0
            total_average_price += average_price if average_price != 'Нет цены' else 0
        except Exception as e:
            print(e)
    return {
        'total_product_weight': round(total_product_weight, 2),
        'total_max_price': round(total_max_price, 2),
        'total_average_price': round(total_average_price / 3, 2),
        'category': category.name or 'Без категории',
        'products': products
    }


class RecipeAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        if self.request.query_params.get('id'):
            queryset = queryset.get(id=self.request.query_params.get('id'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if self.request.query_params.get('id'):
            serializer = self.get_serializer(queryset)
            recipe = update_serialize_data(serializer.data)
            recipe['id'] = serializer.data['id']
            recipe['name'] = serializer.data['name']
            recipe['description'] = serializer.data['description']
            recipe['image'] = serializer.data['image']
            return Response(recipe)
        serializer = self.get_serializer(queryset, many=True)
        print('many')

        for recipe in serializer.data:
            result = update_serialize_data(recipe)
            recipe['total_product_weight'] = result['total_product_weight']
            recipe['total_max_price'] = result['total_max_price']
            recipe['total_average_price'] = result['total_average_price']
            recipe['category'] = result['category']

            recipe['products'] = result['products']

        return Response(serializer.data)
