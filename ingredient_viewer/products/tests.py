from django.test import TestCase


# Create your tests here.
from .models import Product
from .factories import ProductFactory


class ProductTest(TestCase):
    """
    This class represents unittests for the Products model.
    """
    def test_create_product(self):
        """ Test if a product can be added to and retrieved from the database. """
        test_name = 'testproduct'
        test_product = ProductFactory(product_name=test_name)

        saved_product = Product.objects.get(product_name=test_name)
        self.assertEqual(test_product.pk, saved_product.pk)
