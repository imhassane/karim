from .Base import Base
from django.shortcuts import reverse


class Category(Base):
    
    def get_absolute_url(self):
        return reverse('main:category', kwargs={'slug': self.slug})
