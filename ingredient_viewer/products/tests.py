from django.core.files import File
from django.http import Http404
from django.test import Client
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
        self.test_product = ProductFactory()

    def test_check_saved_product(self):
        """ Test if a product can be added to and retrieved from the database. """

        saved_product = Product.objects.get(product_name=self.test_product.product_name)
        self.assertEqual(self.test_product.pk, saved_product.pk)

    def test_retrieve_saved_product(self):
        """ Test if all the properties of a product are saved"""

        saved_product = Product.objects.get(product_name=self.test_product.product_name)
        self.assertEqual(self.test_product.product_name, saved_product.product_name)
        self.assertEqual(self.test_product.ingredients, saved_product.ingredients)


class ViewTest(TestCase):
    """
    This class represents unittests for the different view functions.
    """

    def setUp(self):
        self.client = Client()
        self.url = '/products/overview'

    def test_empty_list(self):
        """ This test should fail if no product was added. """
        response = self.client.get(self.url)
        expected_status_code = 404
        self.assertEqual(response.status_code, expected_status_code)

    def test_list_with_elements(self):
        """ This test should succeed when a product is added. """
        ProductFactory()
        response = self.client.get(self.url)
        expected_status_code = 200
        self.assertEqual(response.status_code, expected_status_code)
