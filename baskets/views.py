from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required  # для декоратора

from products.models import Product
from baskets.models import Basket


# при нажатии отправить в корзину
@login_required  # добавление логики для функции basket_add (в части работы с неавторизованным пользователем))
# Декоратор для представлений, который проверяет, что пользователь вошел в систему, перенаправляя
# при необходимости, на страницу авторизации.
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)  # товар, который добавляем в корзину
    baskets = Basket.objects.filter(user=request.user, product=product)  # добавлен ли товар в корзину для данного user

    if not baskets.exists():  # если товара нет в корзине
        Basket.objects.create(user=request.user, product=product, quantity=1)  # создаем товар для пользователя
        return HttpResponseRedirect(request.META['HTTP_REFERER'])  # возвращает на страницу где было выполнено действие

    else:
        basket = baskets.first()  # если есть, количество товара увеличивается
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
