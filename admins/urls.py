from django.urls import path

from admins.views import index, UserCreateView, UserListView, UserUpdateView, UserDeleteView,\
    admin_products_category


app_name = 'baskets'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),  # для классов вместо id pk
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin_products_category/', admin_products_category, name='admin_products_category')

]
