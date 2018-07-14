from django.db import models
from main.models import Product


# Create your models here.
class Base(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Order(Base):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
