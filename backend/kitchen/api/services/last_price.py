from django.db.models import F, Avg, Case, FloatField, Max, Subquery, OuterRef, Q
from ...models import ProductInStore


def get_max_average_price():
    last_three_records = ProductInStore.objects.filter(
        product=OuterRef('product'),
    ).order_by('-id')[:3]

    last_average_max_price = ProductInStore.objects.annotate(
        last_three_records=Subquery(last_three_records.values('id'))
    ).filter(
        id__in=Subquery(last_three_records.values('id'))
    ).values(
        'product__name', 'store__name', 'product__unit', 'transaction_type'
    ).annotate(
        max_last_3_prices=Max(
            Case(
                default=F('price'),
                output_field=FloatField(),
                when=Q(id__in=Subquery(last_three_records.values('id')))
            )
        )
    ).annotate(
        average_last_3_prices=Avg(
            Case(
                default=F('price'),
                output_field=FloatField(),
                when=Q(id__in=Subquery(last_three_records.values('id')))
            )
        )
    ).order_by('product__name', 'store__name')

    return last_average_max_price
