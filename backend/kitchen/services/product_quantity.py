from django.db.models import Sum
from ..models import ProductInStore, Recipe
from ..api.serializers import ProductInStoreSerializer
from rest_framework.response import Response


def get_product_quantity_for_recipe(recipe_id):
    products = Recipe.objects.get(id=recipe_id).products.all()
    return products
