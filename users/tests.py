from django.test import TestCase
from django.test.client import Client
from users.models import User
from django.core.management import call_command
from django.conf import settings


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('django2', 'django2@geekshop.local', 'geekbrains')

        self.user = User.objects.create_user('tarantino', 'tarantino@geekshop.local', 'geekbrains')

        self.user_with__first_name = User.objects.create_user('umaturman', 'umaturman@geekshop.local', 'geekbrains',
                                                              first_name='Ума')


def test_user_login(self):
    # главная без логина
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.context['user'].is_anonymous)
    self.assertEqual(response.context['title'], 'главная')
    self.assertNotContains(response, 'Пользователь', status_code=200)

    self.client.login(username='tarantino', password='geekbrains')

    # логинимся
    response = self.client.get('/auth/login/')
    self.assertFalse(response.context['user'].is_anonymous)
    self.assertEqual(response.context['user'], self.user)

    # главная после логина
    response = self.client.get('/')
    self.assertContains(response, 'Пользователь', status_code=200)
    self.assertEqual(response.context['user'], self.user)
    # self.assertIn('Пользователь', response.content.decode())


def tearDown(self):
    call_command('sqlsequencereset', 'products', 'users', 'ordersapp', 'baskets')


def test_basket_login_redirect(self):
    # без логина должен переадресовать
    response = self.client.get('/basket/')
    self.assertEqual(response.url, '/auth/login/?next=/basket/')
    self.assertEqual(response.status_code, 302)

    # с логином все должно быть хорошо
    self.client.login(username='tarantino', password='geekbrains')

    response = self.client.get('/basket/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(list(response.context['basket']), [])
    self.assertEqual(response.request['PATH_INFO'], '/basket/')

    # self.assertIn('Ваша корзина, Пользователь', response.content.decode())


def test_user_logout(self):
    # данные пользователя
    self.client.login(username='tarantino', password='geekbrains')

    # логинимся
    response = self.client.get('/auth/login/')
    self.assertEqual(response.status_code, 200)
    self.assertFalse(response.context['user'].is_anonymous)

    # выходим из системы
    response = self.client.get('/auth/logout/')
    self.assertEqual(response.status_code, 302)

    # главная после выхода
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.context['user'].is_anonymous)


def test_user_register(self):
    # логин без данных пользователя
    response = self.client.get('/auth/register/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context['title'], 'регистрация')
    self.assertTrue(response.context['user'].is_anonymous)

    new_user_data = {
        'username': 'samuel',
        'first_name': 'Сэмюэл',
        'last_name': 'Джексон',
        'password1': 'geekbrains',
        'password2': 'geekbrains',
        'email': 'sumuel@geekshop.local',
    }

    response = self.client.post('/auth/register/', data=new_user_data)
    self.assertEqual(response.status_code, 302)

    new_user = User.objects.get(username=new_user_data['username'])

    activation_url = f"{settings.DOMAIN_NAME}/auth/verify/{new_user_data['email']}/{new_user.activation_key}/"

    response = self.client.get(activation_url)
    self.assertEqual(response.status_code, 200)

    # данные нового пользователя
    self.client.login(username=new_user_data['username'], password=new_user_data['password1'])

    # логинимся
    response = self.client.get('/auth/login/')
    self.assertEqual(response.status_code, 200)
    self.assertFalse(response.context['user'].is_anonymous)

    # проверяем главную страницу
    response = self.client.get('/')
    self.assertContains(response, text=new_user_data['first_name'], status_code=200)
