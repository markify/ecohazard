"""Team 7 - URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
# Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('hazard/', include('hazard.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import hazard.views as hazard_views
from rest_framework.urlpatterns import format_suffix_patterns

# path is an alternative way to do url in django 2.0
# path ( website /  ,)   
# import hazard.views as hazard_views    gets hazard -> views.py  make it called hazard_views

urlpatterns = [
<<<<<<< HEAD
=======
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^about(-\w*)?/?$', hello.views.about, name='about'),
    url(r'^map(?:\.html?)?/?$', hello.views.map, name='map'),
    url(r'^signup', hello.views.signup, name='signup'),
    url(r'^login', hello.views.login, name='login'),
    url(r'^report', hello.views.post_report, name='report'),
    url(r'^process_new_report', hello.views.process_new_report, name='process_new_report'),
    url(r'^search', hello.views.search, name='search'),
>>>>>>> master
    path('admin/', admin.site.urls),
    path('', include('hazard.urls')),
    path('captcha/', include('captcha.urls')),
    path('hazardposts/', hazard_views.AllHazardReportAPI.as_view(),
         name="allhazardreportapi"),
    path('hazardreport/<int:hazardreport_id>', hazard_views.hazardreportAPI,
         name="hazardreportapi"),
    path('userpostlist/<int:user_id>', hazard_views.userHazardPostListAPI, name="userpostlist"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
