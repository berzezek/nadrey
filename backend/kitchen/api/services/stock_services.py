from django.db.models import F, Sum, Avg, Case, When, FloatField, Max
from rest_framework.views import APIView
from rest_framework.response import Response
from ...models import ProductInStore


class StockBalanceAPIView(APIView):
    def get(self, request):
        # Получаем остатки продуктов на складе, сгруппированные по продукту и складу
        product_quantities = ProductInStore.objects.values(
            'product__name', 'store__name', 'product__unit', 'transaction_type'
        ).annotate(
            total_quantity=Sum(
                Case(
                    When(transaction_type='in', then=F('quantity')),
                    default=F('quantity') * -1,
                    output_field=FloatField()
                )
            )
        )

        # Получаем среднюю цену последних 3-х покупок
        last_prices = ProductInStore.objects.filter(
            price__isnull=False
        ).order_by('-id')[:3]

        average_price = last_prices.aggregate(avg_price=Avg('price'))['avg_price']

        # Получаем максимальную цену
        max_price = ProductInStore.objects.filter(
            price__isnull=False
        ).aggregate(max_price=Max('price'))['max_price']

        # Объединяем данные в одну сводную таблицу
        stock_balance = {}
        for product_quantity in product_quantities:
            product_name = product_quantity['product__name']
            store_name = product_quantity['store__name']
            total_quantity = product_quantity['total_quantity']
            product_unit = product_quantity['product__unit']

            if product_name not in stock_balance:
                stock_balance[product_name] = {}

            stock_balance[product_name][store_name] = {
                'quantity': total_quantity,
                'last_price': None,
                'unit': product_unit,
            }

        # Преобразуем данные в нужный формат для вывода
        balance_data = []
        for product_name, stores in stock_balance.items():
            for store_name, data in stores.items():
                balance_data.append({
                    'product': product_name,
                    'store': store_name,
                    'quantity': data['quantity'],
                    'max_price': max_price or 0,
                    'average_price': average_price or 0,
                    'unit': data['unit'],
                })
        return Response(balance_data)
