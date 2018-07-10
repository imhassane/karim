from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from main.models import Product, Category


def product_list(request, page=1):

    context = {}

    datas, products = {}, []

    categories = Category.objects.filter(visible=True)

    for category in categories:
        
        datas[category.name] = Product.objects.filter(category=category, visible=True)
        products.extend(list(datas[category.name]))

    context['datas'] = datas

    # Pagination.
    paginator = Paginator(products, 2)

    try:
        context['paginator'] = paginator.page(page)
    
    except EmptyPage:
        context['paginator'] = paginator.page(paginator.num_pages)

    return render(request, 'product_list.html', context)
