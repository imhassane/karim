from django.shortcuts import render, get_object_or_404 as _g
from main.models import Product

def product_detail(request, slug):

    if request.POST:
        pass
    
    else:
        context = {}

        product = _g(Product, slug=slug)

        context['product'] = product

        return render(request, 'product_detail.html', context)
