from django.shortcuts import render
from anketa.myforms import NashaForma
from django.http import HttpResponse

# Create your views here.


def index(req):
    return render(req, 'index.html')


def forma1(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        num = req.POST.get('num')
        out = '<h1>Спасибо</h1>' \
              '<h2>Ваше имя - {0}</h2>' \
              '<h2>Ваше число - {1}</h2>'.format(name, num)
        return HttpResponse(out)
    else:
        anketa1 = NashaForma()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)


def forma2(req):
    pass


