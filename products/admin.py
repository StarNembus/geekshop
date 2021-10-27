from django.contrib import admin
from products.models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    ordering = ('name', )  # сортировка названия по алфавиту
    search_fields = ('name', )  # поиск по полю name
