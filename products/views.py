from datetime import date

from django.shortcuts import render

from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # для кнопок внизу
from django.conf import settings
from django.core import cache
from django.views.decorators.cache import cache_page

# Create your views here.
# views(функции) = контроллеры


def index(request):
    content = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
        'date': date.today()
    }
    return render(request, 'products/index.html', content)


# def get_links_menu():
#     if settings.LOW_CACHE:
#         key = 'links_menu'
#         links_menu = cache.get(key)
#         if links_menu is None:
#             links_menu = ProductCategory.objects.filter(is_active=True)
#             cache.set(key, links_menu)
#         return links_menu
#     else:
#         return ProductCategory.objects.filter(is_active=True)
#
#
# def get_category(pk):
#    if settings.LOW_CACHE:
#        key = f'category_{id}'
#        category = cache.get(key)
#        if category is None:
#            category = get_object_or_404(ProductCategory, id=id)
#            cache.set(key, category)
#        return category
#    else:
#        return get_object_or_404(ProductCategory, id=id)
#
#
# def get_products():
#    if settings.LOW_CACHE:
#        key = 'products'
#        products = cache.get(key)
#        if products is None:
#            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
#            cache.set(key, products)
#        return products
#    else:
#        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
#
#
#
# def get_products_orederd_by_price():
#    if settings.LOW_CACHE:
#        key = 'products_orederd_by_price'
#        products = cache.get(key)
#        if products is None:
#            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
#            cache.set(key, products)
#        return products
#    else:
#        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
#
#
# def get_products_in_category_orederd_by_price(id):
#    if settings.LOW_CACHE:
#        key = f'products_in_category_orederd_by_price_{id}'
#        products = cache.get(key)
#        if products is None:
#           products = Product.objects.filter(category_id=id, is_active=True,
#                                                             \category__is_active=True).order_by('price')
#            cache.set(key, products)
#        return products
#    else:
#        return Product.objects.filter(category__id=id, is_active=True, category__is_active=True).order_by('price')

@cache_page(3600)
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
        products_paginator = paginator.page(1)  # если пришли данные не целочисленного типа направить на 1 страницу
    except EmptyPage:  # если пришла пустая страница
        products_paginator = paginator.page(paginator.num_pages)  # отображаются все страницы(объекты)
    context['products'] = products_paginator  # с помощью paginator добавились дополнительные методы в список products
    return render(request, 'products/products.html', context)
