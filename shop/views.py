from django.shortcuts import render, get_object_or_404
from .models import Mobile, Laptop
from random import shuffle
# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse



def _404(request, ex = None):
    return render(request, '404.html')


def index(request):
    mobiles = list(Mobile.objects.all())
    laptops = list(Laptop.objects.all())
    products = mobiles + laptops
    shuffle(mobiles)
    shuffle(laptops)
    shuffle(products)

    return render(request, 'index.html',{
        'mobiles': mobiles[:5],
        'laptops': laptops[:5],
        'products': products[:5],
        })


def product(request, url):

    mobile = Mobile.objects.filter(link=url+'/')
    laptop = Laptop.objects.filter(link=url+'/')

    if len(mobile):
        product = mobile[0]
        products = list(Mobile.objects.all())

    elif len(laptop):
        product = laptop[0]
        products = list(Laptop.objects.all())
        
    
    else:
        _404(request)

    shuffle(products)

    return render(request, 'product.html', {
        'product': product,
        'products': products[:5],
        })

