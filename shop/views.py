from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from requests import get



def index(request):
    name = request.COOKIES.get('name')

    if not name:
        # do something
        pass

    if request.method == 'POST':
        if 'name' in dict(request.POST.items()):
            if request.POST['name'].replace(' ', '') != '':
                response = HttpResponseRedirect(reverse('/'))
                response.set_cookie('name', request.POST['name'])
                # response.delete_cookie('name')
                return response

        if 'url' in dict(request.POST.items()):
            html = get(request.POST['url']).text
            return HttpResponse(html)

       

    return render(request, 'index.html')


def _404(request, ex = None):
    return render(request, '404.html')
