from unittest.case import TestCase

from mainapp.models import Product


class ProductsTestCase(TestCase):
    def test_product_print(self):
        product_1 = Product.objects.get(name="комфорт 1")
        product_2 = Product.objects.get(name="комфорт 2")
        self.assertEqual(str(product_1), "комфорт 1 (дом)")
        self.assertEqual(str(product_2), "комфорт 2 (дом)")

    def test_product_get_items(self):
        product_1 = Product.objects.get(name="комфорт 1")
        product_3 = Product.objects.get(name="комфорт 2")

        products_as_class_method = set(product_1.get_items())
        products = set([product_1, product_3])

        self.assertIsNotNone(products_as_class_method.intersection(products))
