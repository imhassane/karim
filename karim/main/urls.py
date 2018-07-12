from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    
    path('products/<int:page>/', product_list, name='products'),
    path('product/<slug:slug>/', product_detail, name='product'),
    path('like/product/<slug:slug>/', like_product, name='like'),

    path('search/', search, name='search'),
]