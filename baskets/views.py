from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Basket


# при нажатии отправить в корзину
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)  # товар, который добавляем в корзину
    baskets = Basket.objects.filter(user=request.user, product=product)  # добавлен ли товар в корзину для данного user

    if baskets.exists(): # если товара нет в корзине
        Basket.objects.create(user=request.user, product=product, quantity=1)  # создаем товар для пользователя
        return HttpResponseRedirect(request.META['HTTP_REFERER'])  # возвращает на страницу где было выполнено действие

    else:
        basket = baskets.first()  # если есть, количество товара увеличивается
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
