from django.shortcuts import render, get_object_or_404
from .models import Mobile, Laptop, Header, Special_Off
from random import shuffle
# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse



def _404(request, ex = None):
    return render(request, '404.html')


def index(request):
    mobiles = list(Mobile.objects.all())
    shuffle(mobiles)

    laptops = list(Laptop.objects.all())
    shuffle(laptops)

    products = list(Mobile.objects.order_by('-views')[:3])
    products += list(Laptop.objects.order_by('-views')[:3])
    shuffle(products)

    headers = Header.objects.all()

    special_off = Special_Off.objects.all().first()
    off_price = int(special_off.price * (100 - special_off.off) / 100)
    time_left = 1531.30 # now - special_off.time

    return render(request, 'index.html',{
        'mobiles': mobiles[:5],
        'laptops': laptops[:5],
        'products': products[:5],
        'headers': headers,
        'special_off': special_off,
        'off_price': off_price,
        'time_left': time_left,
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


    product.views += 1
    product.save()

    shuffle(products)

    return render(request, 'product.html', {
        'product': product,
        'products': products[:5],
        })

