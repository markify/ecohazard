from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')


def about(request, extra=None):
    switcher = {
        '-ali': 'about/about-ali.html',
        '-cameron': 'about/about-cameron.html',
        '-girish': 'about/about-girish.html',
        '-humeston': 'about/about-humeston.html',
        '-larsen': 'about/about-larsen.html',
        '-mark': 'about/about-mark.html',
        '-sutherland': 'about/about-sutherland.html'
    }
    if extra:
        return render(request, switcher.get(extra, 'about.html'))
    return render(request, 'about.html')


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def marker(request):
    return render(request, 'marker.html')


def map(request):
    return render(request, 'map.html')


def search(request):
    return render(request, 'search.html')
