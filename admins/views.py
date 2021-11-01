from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import User
from products.models import ProductCategory
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, AdminProductCategory
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_staff)  # ограничение для входа в админку
def index(request):
    context = {'title': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# CRUD
# create
class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')


# create
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#
#     context = {'title': 'GeekShop - Создание пользователей', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


# read
class UserListView(ListView):  # User - модель от которой наследуется, ListView - класс от которого наследуется
    model = User
    template_name = 'admins/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# # read
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'GeekShop - Пользователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


# update

class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Редакирование пользователя'
        return context


# update
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'GeekShop - Обновление пользователя',
#                'form': form,
#                'selected_user': selected_user,
#                }
#     return render(request, 'admins/admin-users-update-delete.html', context)


# delete
class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')



    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.safe_delete()
        return HttpResponseRedirect(success_url)

# delete (обработчик действия)
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.safe_delete()  # заблокировать
#     return HttpResponseRedirect(reverse('admins:admin_users'))


def admin_products_category(request):
    category = ProductCategory.objects.all()
    context = {
        'title': 'GeekShop - Category',
        'category': category,
    }
    return render(request, 'admins/admin_products_category.html', context)
