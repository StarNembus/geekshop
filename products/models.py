from django.db import models

# Create your models here.
# модели = таблицы в БД


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):  # переопределяем метод для вывода значения в консоли в нужном нам формате
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # decimal_places = сколько цифр после запятой
    quantity = models.PositiveIntegerField(default=0)  # количество не должно быть отрицательным числом
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # связь с таблицей ProductCategory

    def __str__(self):
        return f'{self.name} | {self.category.name}'  # название | название категории


    # def get_items():
        #     return Product.objects.filter(is_active=True).order_by('category', 'name')



