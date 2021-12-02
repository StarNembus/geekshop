from django.test import TestCase
from products.models import Product, ProductCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name='Верхняя одежда')
        self.product_1 = Product.objects.create(name='Куртка', category=category, price=3000, quantity=3)
        self.product_2 = Product.objects.create(name='Шуба', category=category, price=50000, quantity=5)

    def test_product_get(self):
        product_1 = Product.objects.get(name='Куртка')
        product_2 = Product.objects.get(name='Шуба')
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name='Куртка')
        product_2 = Product.objects.get(name='Шуба')
        self.assertEqual(str(product_1), 'Куртка(Верхняя одежда)')
        self.assertEqual(str(product_2), 'Шуба(Верхняя одежда)')

    def test_product_get_items(self):
        product_1 = Product.objects.get(name='Куртка')
        product_2 = Product.objects.get(name='Шуба')
        products = product_1.get_items()

        self.assertEqual(list(products), [product_1, product_2])
