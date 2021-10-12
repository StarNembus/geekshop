from datetime import date

from django.shortcuts import render

from products.models import ProductCategory, Product


# Create your views here.
# views(функции) = контроллеры


def index(request):
    content = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
        'date': date.today()
    }
    return render(request, 'products/index.html', content)


def products(request):
    content_product = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', content_product)
