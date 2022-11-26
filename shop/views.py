from django.shortcuts import render
from .models import Category, Product, Image
from random import shuffle
# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    categories = Category.objects.all()
    products = list(Product.objects.all())
    images = Image.objects.all()
    
    shuffle(products)

    return render(request, 'index.html', {
        'categories': categories,
        'products':products,
        'images': images
        })


def _404(request, ex = None):
    return render(request, '404.html')
