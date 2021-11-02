from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import ProductCategory
from django.forms import ModelForm
from products.models import Product


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))


class AdminProductCategory(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class AdminProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class AdminProductCreate(ModelForm):

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'description', 'category', 'quantity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''