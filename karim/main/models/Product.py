from django.db import models
from .Base import Base
from .Category import Category


class Product(Base):

    price = models.PositiveSmallIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default=0)

    # Dimensions du produit
    width = models.PositiveSmallIntegerField(default=0)
    length = models.PositiveSmallIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=0)
    ray = models.PositiveSmallIntegerField(default=0)

    # Disponibilité du produit.
    address = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=100)
    availability = models.DateField()

    # Catégories du produit
    category = models.ManyToManyField(Category, related_name='products')