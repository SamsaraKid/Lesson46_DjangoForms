from django.shortcuts import render
from anketa.myforms import * #NashaForma, Forma2, Uploadforma
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
    if req.method == 'POST':
        k1 = req.POST.get('k1')
        k2 = req.POST.get('k2')
        k4 = req.POST.get('k4')
        k7 = req.POST.get('k7')
        k10 = req.POST.get('k10')
        print(k1, k2, k4, k7)
        out = '<h1>Спасибо</h1>' \
              '<h2>Число - {0}</h2>' \
              '<h2>Почта - {1}</h2>' \
              '<h2>Ответ - {2}</h2>' \
              '<h2>Язык - {3}</h2>'.format(k1, k2, k4, k10)
        return HttpResponse(out)
    else:
        anketa = Forma2()
        data = {'form': anketa}
        return render(req, 'forma.html', data)


def upload(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        img = req.FILES.get('img').read()
        file = open('anketa/static/upload/{0}.jpg'.format(name), 'wb')
        file.write(img)
        file.close()
        fpath = 'upload/{0}.jpg'.format(name)
        data = {'k1': name, 'k2': fpath}
        return render(req, 'endpage.html', context=data)
    else:
        anketa = Uploadforma()
        data = {'form': anketa}
        return render(req, 'forma.html', data)

