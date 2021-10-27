from django.shortcuts import render
from django.urls import reverse
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from django.shortcuts import render, HttpResponseRedirect


def index(request):
    context = {'title': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# CRUD

# create
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()

    context = {'title': 'GeekShop - Создание пользователей', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


# read
def admin_users(request):
    context = {
        'title': 'GeekShop - Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


# update
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'GeekShop - Обновление пользователя',
               'form': form,
               'selected_user': selected_user,
               }
    return render(request, 'admins/admin-users-update-delete.html', context)


# delete (обработчик действия)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.safe_delete()  # заблокировать
    return HttpResponseRedirect(reverse('admins:admin_users'))
