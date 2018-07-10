from django.urls import path
from main.views import *


urlpatterns = [
    path('', product_list, name='products'),
    path('product/<slug:slug>/', product_detail, name='product'),
]