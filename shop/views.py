from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect #, HttpResponse



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
       

    return render(request, 'index.html')


def _404(request, ex = None):
    return render(request, '404.html')
