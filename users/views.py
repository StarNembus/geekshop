from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages


def login(request):
    if request.method == 'POST':  # для валидации данных
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # аутентфикация пользователя
            if user and user.is_active:  # если пользователь есть в системе
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))  # user перенаправляется на главную страницу
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful registration!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


