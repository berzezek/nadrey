def get_total_count(obj, model_name, field_name, my_str):
    total = 0
    for product in obj.products.all():
        print(product.__dict__)
        try:
            count = model_name.objects.get(product=product.product_id)[field_name]
            total += count
        except model_name.DoesNotExist:
            return f'{my_str}: {product.product}'

    return total