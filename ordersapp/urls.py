from django.urls import path
from ordersapp.views import OrderList, OrderCreate, OrderUpdate, OrderDelete, OrderRead

import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    path('read/<int:pk>/', OrderRead.as_view(), name='order_read'),
    path('forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
    path('create/', OrderCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', ordersapp.get_product_price),
]
