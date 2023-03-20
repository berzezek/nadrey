from django.db.models import F, Sum, Case, When, FloatField
from rest_framework.views import APIView
from rest_framework.response import Response
from ...models import ProductInStore
from .last_price import get_max_average_price


class StockBalanceAPIView(APIView):
    def get(self, request):
        # Получаем последние 3 записи по каждому продукту
        balanced_product = get_max_average_price()

        # Получаем остаток продукта на складе
        product_quantity = ProductInStore.objects.values(
            'product__name', 'store__name', 'transaction_type'
        ).annotate(
            product_quantity=Sum(
                Case(
                    When(transaction_type='in', then=F('quantity')),
                    default=F('quantity') * -1,
                    output_field=FloatField()
                )
            )
        )

        for pq in product_quantity:
            for bp in balanced_product:
                if pq['product__name'] == bp['product__name'] \
                        and pq['store__name'] == bp['store__name']:
                    pq['max_price'] = bp['max_last_3_prices']
                    pq['average_price'] = bp['average_last_3_prices']
                    pq['unit'] = bp['product__unit']
                    break


        return Response(product_quantity)
