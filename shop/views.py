from .models import Mobile, Laptop, Header, SpecialOff,\
     Product, Image, Category, Brand, Detail, Account, Session
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now
from django.db.utils import IntegrityError
from random import shuffle
from secrets import token_urlsafe

# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse


def _404(request, ex=None):
    return render(request, '404.html')


def index(request):
    try:
        account = Session.objects.get(session=request.session['user-session']).user
    except (ObjectDoesNotExist, KeyError):
        account = None

    mobiles = Mobile.objects.order_by('?')[:10]

    laptops = Laptop.objects.order_by('?')[:10]

    products = list(Product.objects.order_by('-views')[:10])
    most_view = []

    for _product in products:
        if _product.category.name == 'Mobile':
            mobile = Mobile.objects.get(product__name=_product.name)
            most_view.append(mobile)

        if _product.category.name == 'Laptop':
            laptop = Laptop.objects.get(product__name=_product.name)
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
        'account': account,
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
    _product = get_object_or_404(Product, name__iexact=url)
    __product = eval(f'{_product.category.name}.objects.get(product__name__iexact=_product.name)')
    products = eval(f'{_product.category.name}.objects.order_by("?")[:10]')

    details = Detail.objects.filter(product=_product)
    
    _product.views += 1
    _product.save()

    images = Image.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    try:
        account = Session.objects.get(session=request.session['user-session']).user
    except (ObjectDoesNotExist, KeyError):
        account = None

    context = {
        'account': account,
        'title': __product.product,
        'product': __product,
        'products': products,
        'images': images,
        'brands': brands,
        'categories': categories,
        'details': details,
    }

    return render(request, 'product.html', context)


def categories_and_brands(request, url):
    try:
        group = Category.objects.get(name__iexact=url)
        products = eval(f'{group.name}.objects.order_by("?")[:21]')

    except ObjectDoesNotExist:
        group = get_object_or_404(Brand, name__iexact=url)
        products = []
        for cat in Category.objects.all():
            products += list(eval(f'{cat.name}.objects.filter(product__brand__name__iexact=url)[:21]'))
            shuffle(products)

    images = Image.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    try:
        account = Session.objects.get(session=request.session['user-session']).user
    except (ObjectDoesNotExist, KeyError):
        account = None

    context = {
        'account': account,
        'title': 'محصولات ' + group.persian_name,
        'products': products[:21],
        'images': images,
        'brands': brands,
        'categories': categories,
        'group': group.persian_name,
    }

    return render(request, 'custom.html', context)


def search(request):
    query = request.GET.get('q')

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

    try:
        account = Session.objects.get(session=request.session['user-session']).user
    except (ObjectDoesNotExist, KeyError):
        account = None

    context = {
        'account': account,
        'title': 'نتایج جستجو',
        'products': products[:21],
        'images': images,
        'brands': brands,
        'categories': categories,
        'query': query,
    }

    return render(request, 'custom.html', context)


def login(request):
    redir = request.GET.get("redirect") if request.GET.get("redirect") else '/'

    try:
        Session.objects.get(session=request.session['user-session'])
        return redirect(redir)
    except (ObjectDoesNotExist, KeyError):
        pass
    
    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        'error': '',
        'brands': brands,
        'categories': categories,
        }
    
    if request.method == 'POST':
        _name = request.POST.get('name')
        _pass = request.POST.get('password')
        _email = request.POST.get('email')

        token = token_urlsafe()

        if _name:
            if _name.replace(' ','') == '':
                context['error'] = 'نام و نام خوانوادگی خالی است!'
                return render(request, 'login.html', context)

            elif len(_pass) < 8 or ' ' in _pass or \
                (_pass.lower() != _pass != _pass.upper() and not any([c.isdigit() for c in _pass])):
                context['error'] = 'کلمه عبور باید بدون فاصله و ترکیبی از اعداد و حروف کوچک و بزرگ و حداقل ۸ کاراکتر باشد!'
                return render(request, 'login.html', context)

            try:
                account = Account(
                    name=_name,
                    email=_email,
                    password=_pass,
                    )
                account.save()

            except IntegrityError:
                context['error'] = 'اکانت با این ایمیل موجود است لطفا وارد شوید!'
                return render(request, 'login.html', context)

        else:
            try:
                account = Account.objects.get(email=_email)
                if account.password != _pass:
                    context['error'] = 'کلمه عبور اشتباه است!'
                    return render(request, 'login.html', context)

            except ObjectDoesNotExist:
                context['error'] = 'ایمیل موجود نیست! لطفا اکانت بسازید.'
                return render(request, 'login.html', context)

        session = Session(
                user=account,
                session=token,
                description=request.META['HTTP_USER_AGENT'],
                )
        session.save()

        request.session['user-session'] = token

        return redirect(redir)

    return render(request, 'login.html', context)
