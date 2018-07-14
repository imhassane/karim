from django.shortcuts import render, get_object_or_404 as _g
from shop.models import Order
from main.models import Product

from django.http import JsonResponse
from django.utils.text import slugify


# Create your views here.
def add_to_bucket(request, product_pk):

    
    product = _g(Product, pk=product_pk)

    order = Order(product=product)
    order.save()

    bucket = request.session['bucket']
    bucket.append(order.pk)

    request.session['bucket'] = bucket

    return JsonResponse({
        'message': "Votre commande a été ajoutée",
        "order_count": len(request.session['bucket'])
    })

def del_from_bucket(request, order_pk):
    
    order = _g(Order, pk=order_pk)
    
    bucket = request.session['bucket']
    bucket.remove(order_pk)

    request.session['bucket'] = bucket
    
    order.delete()

    return JsonResponse({
        'message': "La commande a été supprimée"
    })

def bucket(request):
    
    context = {}

    try:

        bucket = [_g(Order, pk=pk) for pk in request.session['bucket']]
        context['bucket'] = bucket
        context['total_price'] = sum([x.product.price for x in bucket]) if len(bucket) > 0 else 0
    
    except:

        del request.session['bucket']

    return render(request, "bucket.html", context)