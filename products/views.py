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


def products(request, category_id=None):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context['products'] = products
    return render(request, 'products/products.html', context)
