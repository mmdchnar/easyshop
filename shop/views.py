from django.shortcuts import render
# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, 'index.html')


def _404(request, ex = None):
    return render(request, '404.html')
