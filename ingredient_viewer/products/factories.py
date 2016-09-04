import factory

from . import models


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Product

    product_name = factory.Sequence(lambda n: 'Product #{}'.format(n))
    ingredients = 'A short list of ingredients'
