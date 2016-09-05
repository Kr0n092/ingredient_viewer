import factory

from . import models


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Product

    product_name = factory.Sequence(lambda n: 'Product #{}'.format(n))
    ingredients = 'butter;cheese;eggs'
    image = factory.django.ImageField(color='orange', format='PNG')
