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
#Name: CSC Team 07
#Description: global urls
#Usage: access routes and links to web pages of hazard reports ,admin,etc..
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
import hazard.views as hazard_views
from rest_framework.urlpatterns import format_suffix_patterns

# path is an alternative way to do url in django 2.0
# path ( website /  ,)   
# import hazard.views as hazard_views    gets hazard -> views.py  make it called hazard_views

 
handler404 = 'hazard.views.handler404' 
handler500 = 'hazard.views.handler500' 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hazard.urls')),
    path('hazardposts/', hazard_views.AllHazardReportAPI.as_view(),
         name="allhazardreportapi"),
    path('hazardreport/<int:hazardreport_id>', hazard_views.hazardreportAPI,
         name="hazardreportapi"),
    path('userpostlist/<int:user_id>', hazard_views.userHazardPostListAPI, name="userpostlist"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
