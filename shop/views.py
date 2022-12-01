from django.shortcuts import render, get_object_or_404
from .models import Mobile, Laptop, Header, Special_Off, Product, Image
from random import shuffle
from django.utils.timezone import now
# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse



def _404(request, ex = None):
    return render(request, '404.html')


def index(request):
    mobiles = list(Mobile.objects.all())
    shuffle(mobiles)

    laptops = list(Laptop.objects.all())
    shuffle(laptops)

    products = list(Product.objects.order_by('-views')[:6])
    most_view = []

    for product in products:
        if product.category.name == 'Mobile':
            mobile = Mobile.objects.get(product__name=product.name)
            most_view.append(mobile)

        if product.category.name == 'Laptop':
            laptop = Laptop.objects.get(product__name=product.name)
            most_view.append(laptop)

    # shuffle(most_view)

    images = Image.objects.all()

    headers = Header.objects.all()

    special_off = Special_Off.objects.all().first()
    off_price = int(special_off.price * (100 - special_off.off) / 100)
    time_left = special_off.time - now()
    time_left = time_left.days * 24*60 + time_left.seconds / 60

    return render(request, 'index.html',{
        'mobiles': mobiles[:5],
        'laptops': laptops[:5],
        'most_view': most_view[:5],
        'images': images,
        'headers': headers,
        'special_off': special_off,
        'off_price': off_price,
        'time_left': time_left,
        })


def product(request, url):

    link = Product.objects.filter(link=url+'/')

    if len(link):

        if link[0].category.name == 'Mobile':
            product = Mobile.objects.get(product__name=link[0].name)
            products = list(Mobile.objects.all())

        if link[0].category.name == 'Laptop':
            product = Laptop.objects.get(product__name=link[0].name)
            products = list(Laptop.objects.all())

    else:
        _404(request)


    link[0].views += 1
    link[0].save()

    shuffle(products)

    images = Image.objects.all()

    return render(request, 'product.html', {
        'product': product,
        'products': products[:5],
        'images': images,
        })
