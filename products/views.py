from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to list all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/store.html', context)


def product_info(request, product_id):
    """ Lists the information of the targeted product """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }

    return render(request, 'products/product_info.html', context)
