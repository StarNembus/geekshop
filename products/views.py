from datetime import date

from django.shortcuts import render

from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # для кнопок внизу


# Create your views here.
# views(функции) = контроллеры


def index(request):
    content = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
        'date': date.today()
    }
    return render(request, 'products/index.html', content)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)  # отображается страница выбранная пользователем
    except PageNotAnInteger:
        products_paginator = paginator.page(1)   # если пришли данные не целочисленного типа направить на 1 страницу
    except EmptyPage:  # если пришла пустая страница
        products_paginator = paginator.page(paginator.num_pages)  # отображаются все страницы(объекты)
    context['products'] = products_paginator  # с помощью paginator добавились дополнительные методы в список products
    return render(request, 'products/products.html', context)
