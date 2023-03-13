from django.db.models import F, Sum, Case, When, FloatField, Max
from rest_framework.views import APIView
from ...models import ProductInStore
from rest_framework.response import Response


class StockBalanceAPIView(APIView):
    def get(self, request, format=None):
        # Получаем остатки продуктов на складе, сгруппированные по продукту и складу
        product_quantities = ProductInStore.objects.values(
            'product__name', 'store__name', 'product__unit'
        ).annotate(
            total_quantity=Sum(
                Case(
                    When(price=None, then=F('quantity') * -1),
                    default=F('quantity'),
                    output_field=FloatField()
                )
            )
        )

        # Получаем максимальную цену продукта на каждом складе
        last_prices = ProductInStore.objects.filter(
            price__isnull=False
        ).values(
            'product__name', 'store__name'
        ).annotate(
            max_price=Max('price')
        )

        # Объединяем данные в одну сводную таблицу
        stock_balance = {}
        for pq in product_quantities:
            product_name = pq['product__name']
            store_name = pq['store__name']
            total_quantity = pq['total_quantity']
            product_unit = pq['product__unit']

            if product_name not in stock_balance:
                stock_balance[product_name] = {}

            stock_balance[product_name][store_name] = {
                'quantity': total_quantity,
                'last_price': None,
                'unit': product_unit,
            }

        for lp in last_prices:
            product_name = lp['product__name']
            store_name = lp['store__name']
            max_price = lp['max_price']

            if product_name in stock_balance and store_name in stock_balance[product_name]:
                stock_balance[product_name][store_name]['max_price'] = max_price

        # Преобразуем данные в нужный формат для вывода
        balance_data = []
        for product_name, stores in stock_balance.items():
            for store_name, data in stores.items():
                balance_data.append({
                    'product': product_name,
                    'store': store_name,
                    'quantity': data['quantity'],
                    'max_price': data['max_price'],
                    'unit': data['unit'],
                })
        return Response(balance_data)
