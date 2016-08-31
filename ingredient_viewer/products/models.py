from django.db import models


# Create your models here.
class Product(models.Model):
    """
    A class that represents information about a product such as:
        - a name
        - ingredients of the product
    """
    product_name = models.TextField(primary_key=True, default='Add product here.')
    ingredients = models.TextField(default='Add ingredients here.')

    def __str__(self):
        return '{}'.format(self.product_name)