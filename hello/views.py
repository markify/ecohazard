from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
    #r = requests.get('http://httpbin.org/status/418')
    #print(r.text)
    #return HttpResponse('<pre>' + r.text + '</pre>')

def about(request):
    return render(request, 'about.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def about1(request):
    return render(request, 'about/about-ali.html')

def about2(request):
    return render(request, 'about/about-cameron.html')
    
def about3(request):
    return render(request, 'about/about-girish.html')

def about4(request):
    return render(request, 'about/about-humeston.html')

def about5(request):
    return render(request, 'about/about-larsen.html')

def about6(request):
    return render(request, 'about/about-mark.html')

def about7(request):
    return render(request, 'about/about-sutherland.html')    