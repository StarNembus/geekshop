from django.urls import path

# from users.views import UserFormView, UserCreateView, profile, logout
from users.views import login, UserCreateView, profile, logout, send_verify_mail, verify

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    # path('login/', UserFormView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('send_verify_mail/<str:email>/<str:activation_key>/', send_verify_mail, name='send_verify_mail'),
    path('verify/<str:email>/<str:activation_key>/', verify, name='verify'),

]
