from django.db.models import Avg, Max
from rest_framework import generics
from rest_framework.response import Response
from ...models import Recipe, ProductInStore, Ingredients, CategoryRecipe

from ..serializers import RecipeSerializer


class RecipeAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Calculate the total price and weight for each recipe
        for recipe in serializer.data:
            category = CategoryRecipe.objects.get(id=recipe['category'])
            products = []
            unit_weight = 1
            total_product_weight = 0
            total_max_price = 0
            total_average_price = 0
            for pk in recipe['products']:
                try:
                    product = Ingredients.objects.get(id=pk)
                    last_prices = ProductInStore.objects.filter(
                        price__isnull=False,
                        product_id=product.product.id,
                    ).order_by('-id')[:3]
                    average_price = last_prices.aggregate(avg_price=Avg('price'))[
                                        'avg_price'] or 'Нет цены'
                    if average_price != 'Нет цены':
                        average_price = average_price * product.quantity

                    max_price = last_prices.aggregate(max_price=Max('price'))[
                                    'max_price'] or 'Нет цены'
                    if max_price != 'Нет цены':
                        max_price = max_price * product.quantity

                    if product.product.unit == 'gr':
                        unit_weight = 1 / 1000 * product.quantity
                    elif product.product.unit == 'kg':
                        unit_weight = product.quantity
                    if product.product.weight:
                        unit_weight = product.product.weight * product.quantity
                    products.append({
                        'id': product.product.id,
                        'name': product.product.name,
                        'quantity': product.quantity,
                        'unit': product.product.unit,
                        'unit_weight': unit_weight,
                        'average_price': average_price,
                        'max_price': max_price,
                    })
                    total_product_weight += unit_weight if unit_weight != 'Нет цены' else 0
                    total_max_price += max_price if max_price != 'Нет цены' else 0
                    total_average_price += average_price if average_price != 'Нет цены' else 0
                except Exception as e:
                    print(e)
            recipe['total_product_weight'] = round(total_product_weight, 2)
            recipe['total_max_price'] = round(total_max_price, 2)
            recipe['total_average_price'] = round(total_average_price, 2)
            recipe['category'] = category.name or 'Без категории'

            recipe['products'] = products

        return Response(serializer.data)
