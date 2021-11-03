from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)  # для загрузки картинки

    def safe_delete(self):
        self.is_active = False
        self.save()  # для def admin_users_delete

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):  # проверка актуальности ключа(когда клю считается истекшим)
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
