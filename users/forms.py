from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:  # передаем в данном классе параметры с которыми будет работать UserLoginForm
        model = User
        fields = ('username', 'password')
