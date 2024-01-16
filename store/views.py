from django.shortcuts import render, get_object_or_404
from .models import Product
from catagory.models import Catagory
from .models import Product
# Create your views here.

def store(request, catagory_slug=None):
    categories = None
    products = None
    if catagory_slug != None:
        categories = get_object_or_404(Catagory, slug=catagory_slug)
        products = Product.objects.filter(category=categories, is_available=True) 
    else:    
        products = Product.objects.all().filter(is_available=True)
    context={'products':products}
    return render(request, 'store.html', context)

def product_detail(request, catagory_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=catagory_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {'single_product':single_product}
    return render(request, 'product_detail.html', context)