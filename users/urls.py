from django.urls import path

# from users.views import UserFormView, UserCreateView, profile, logout
from users.views import login, UserCreateView, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    # path('login/', UserFormView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
