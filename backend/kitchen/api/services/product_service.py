from rest_framework import serializers, viewsets
from rest_framework.response import Response

from ...models import ProductInStore

def group_product(merged_data):
    product_dict = {}
    for data in merged_data:
        if data['product'] not in product_dict:
            product_dict[data['product']] = {
                'quantity': data['quantity'],
                'price': data['price'],
                'date': data['date'] if data['date'] else None
            }
        else:
            if data['transaction_type'] == 'in':
                product_dict[data['product']]['quantity'] += data['quantity']
            else:
                product_dict[data['product']]['quantity'] -= data['quantity']

            if data['price']:
                product_dict[data['product']]['price'] = data['price']

            if data['expiration_date'] and (not product_dict[data['product']]['date'] or data['expiration_date'] >
                                            product_dict[data['product']]['date']):
                product_dict[data['product']]['date'] = data['expiration_date']

    result = []
    for product_id, data in product_dict.items():
        result.append({
            'id': product_id,
            'quantity': data['quantity'],
            'price': data['price'],
            'date': data['date'] if data['date'] else None
        })

    return result

class ProductServiceSerializer(serializers.ModelSerializer):
    """
    Нужно объеденить список записей по продукту и посчитать общее количество
    """
    class Meta:
        model = ProductInStore
        fields = '__all__'



class SomeViews(viewsets.ModelViewSet):
    queryset = ProductInStore.objects.all()
    serializer_class = ProductServiceSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(group_product(data))