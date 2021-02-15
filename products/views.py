from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import Product
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    """ A view to list all products """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/store.html', context)


def product_info(request, product_id):
    """ Lists the information of the targeted product """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }

    return render(request, 'products/product_info.html', context)


def view_purchase(request):
    """ A view that renders the purchase page """

    return render(request, 'products/purchase.html')


def add_for_purchase(request, item_id):
    """ Add a product for purchase """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    purchase = request.session.get('purchase', {})

    if item_id in list(purchase.keys()):
        purchase[item_id] += quantity
    else:
        purchase[item_id] = quantity

    request.session['purchase'] = purchase
    return redirect(redirect_url)


def modify_purchase(request, item_id):
    """ modify product for purchase """

    quantity = int(request.POST.get('quantity'))
    purchase = request.session.get('purchase', {})

    if quantity > 0:
        purchase[item_id] = quantity
    else:
        purchase.pop(item_id)

    request.session['purchase'] = purchase
    return redirect(reverse('view_purchase'))


def remove_product(request, item_id):
    """ modify product for purchase """

    purchase = request.session.get('purchase', {})

    try:
        purchase.pop(item_id)

        request.session['purchase'] = purchase
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
