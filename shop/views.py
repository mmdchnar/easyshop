from django.shortcuts import render, get_object_or_404
from .models import Mobile, Laptop, Header, SpecialOff, Product, Image, Category, Brand
from random import shuffle
from django.utils.timezone import now
from django.contrib.postgres.search import SearchVector


# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse


def _404(request, ex=None):
    return render(request, '404.html')


def index(request):
    mobiles = Mobile.objects.order_by('?')[:10]

    laptops = Laptop.objects.order_by('?')[:10]

    products = list(Product.objects.order_by('-views')[:10])
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
    brands = Brand.objects.all()
    categories = Category.objects.all()

    headers = Header.objects.all()

    special_off = SpecialOff.objects.all().first()
    off_price = int(special_off.price * (100 - special_off.off) / 100)
    time_left = special_off.time - now()
    time_left = time_left.days * 24 * 60 + time_left.seconds / 60

    context = {
        'mobiles': mobiles,
        'laptops': laptops,
        'most_view': most_view[:5],
        'images': images,
        'headers': headers,
        'special_off': special_off,
        'off_price': off_price,
        'time_left': time_left,
        'brands': brands,
        'categories': categories,
    }

    return render(request, 'index.html', context)


def product(request, url):
    url = url.lower() + '/'

    link = Product.objects.filter(link=url)

    if len(link):
        product = eval(f'{link.first().category.name}.objects.get(product__name=link.first().name)')
        products = eval(f'{link.first().category.name}.objects.order_by("?")[:10]')

        link.first().views += 1
        link.first().save()

    else:
        return _404(request)

    images = Image.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        'title': product.product,
        'product': product,
        'products': products,
        'images': images,
        'brands': brands,
        'categories': categories,
    }

    return render(request, 'product.html', context)


def categories_and_brands(request, url):
    url = url.lower() + '/'

    category = Category.objects.filter(link=url)
    brand = Brand.objects.filter(link=url)

    if len(category):
        products = eval(f'{category.first().name}.objects.order_by("?")[:21]')
        group = category.first()

    elif len(brand):
        products = []

        for cat in Category.objects.all():
            products += list(eval(f'{cat.name}.objects.filter(product__brand__link=url)[:21]'))

        shuffle(products)

        group = brand.first()

    else:
        return _404(request)

    images = Image.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        'title': 'محصولات ' + group.persian_name,
        'products': products[:21],
        'images': images,
        'brands': brands,
        'categories': categories,
        'group': group,
    }

    return render(request, 'custom.html', context)


def search(request):
    query = request.GET.get("q")

    if not query:
        return _404(request)

    products = []

    for cat in Category.objects.all():
        vector = SearchVector('product__name',
                              'product__category__name',
                              'product__category__persian_name',
                              'product__brand__name',
                              'product__brand__persian_name',
                              )

        products += list(eval(f'{cat.name}.objects.annotate(search=vector)\
            .filter(search=query)[:21]'))

    shuffle(products)

    images = Image.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        'title': 'نتیجه جستجو',
        'products': products[:21],
        'images': images,
        'brands': brands,
        'categories': categories,
        'query': query,
    }

    return render(request, 'custom.html', context)
