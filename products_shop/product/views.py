from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from product.models import Product
from django.forms import modelform_factory


def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product/detail.html",
                  {"product": product})

def products(request):
    return render(request, "product/products.html",
                  {"products": Product.objects.all()})