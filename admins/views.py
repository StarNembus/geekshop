from django.shortcuts import render


def index(request):
    context = {'title': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# CRUD

# create
def admin_users_create(request):
    context = {'title': 'GeekShop - Создание пользователей'}
    return render(request, 'admins/admin-users-create.html', context)


# read
def admin_users(request):
    context = {'title': 'GeekShop - Пользователи'}
    return render(request, 'admins/admin-users-read.html', context)


# update
def admin_users_update(request):
    context = {'title': 'GeekShop - Обновление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)


# delete (обработчик действия)
def admin_users_delete(request):
    pass
