from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.timezone import now

from .models import HelloGreeting
from .models import HazardTypes
from .models import HazardReports
from .models import User
from .models import HazardTypes

import requests


# Create your views here.
def index(request):
    hazard_reports = HazardReports.objects.all()

    return render(request, 'index.html', {'hazard_reports': hazard_reports})


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


def post_report(request):
    hazard_types = HazardTypes.objects.all()

    return render(request, 'report.html', {'hazard_types': hazard_types})


def process_new_report(request):
    report_data = request.POST

    hazard_report = HazardReports(
        description=report_data['description'],
        status=1,
        priority=1,
        address_id='NULL',
        street=report_data['street_number'] + ' ' + report_data['route'],
        city=report_data['locality'],
        state=report_data['administrative_area_level_1'],
        zip_code=report_data['postal_code'],
        country=report_data['country'])

    hazard_report.creator = User.objects.get(id=report_data['creator'])
    hazard_report.hazard_type = HazardTypes.objects.get(id=report_data['hazard_type'])
    hazard_report.assigned_to = User.objects.get(id=report_data['creator'])

    hazard_report.save()

    # hazard_reports = HazardReports.objects.all()
    return redirect('index')
    # return render(request, 'index.html', {'hazard_reports': hazard_reports})


def map(request):
    return render(request, 'map.html')


def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
    
def report(request):
    return render(request, 'report.html')


def search(request):
    return render(request, 'search.html')
