from django.core.files import File
from django.test import TestCase


# Create your tests here.
from unittest import mock

from .models import Product
from .factories import ProductFactory


class ProductTest(TestCase):
    """
    This class represents unittests for the Products model.
    """
    def setUp(self):
        test_name = 'testproduct'
        test_ingredient = 'butter, cheese, eggs'

        self.test_product = ProductFactory(product_name=test_name, ingredients=test_ingredient)

    def test_check_saved_product(self):
        """ Test if a product can be added to and retrieved from the database. """

        saved_product = Product.objects.get(product_name=self.test_product.product_name)
        self.assertEqual(self.test_product.pk, saved_product.pk)

    def test_retrieve_saved_product(self):
        """ Test if all the properties of a product are saved"""

        saved_product = Product.objects.get(product_name=self.test_product.product_name)
        self.assertEqual(self.test_product.product_name, saved_product.product_name)
        self.assertEqual(self.test_product.ingredients, saved_product.ingredients)