from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductCategory, Product, ProductInStore, Ingredients, CategoryRecipe, Recipe


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'calories', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

    def image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')


class ProductInStoreAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'date', 'expiration_date', 'quantity', 'price')
    search_fields = ('product',)


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'quantity')
    search_fields = ('product',)


class CategoryRecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInStore, ProductInStoreAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(CategoryRecipe, CategoryRecipeAdmin)
admin.site.register(Recipe, RecipeAdmin)
