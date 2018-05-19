#Name: CSC Team 07
#Description: url and routes
#Usage: the website address and link
from django.urls import path, re_path
from . import views

# APP NAME AND URL PATHING / ROUTES

#  (path  link/url   ,  (views.py).Class/Definition  ,  name)
#  use re_path to read regex expression alternative to url regex

app_name = "ecohazards"
urlpatterns = [
        path("", views.index, name="index"),
        path("register/", views.UserFormView.as_view(), name='register'),
        path("login_process/", views.login_process, name='login_process'),
        path("logout/", views.logout_process, name="logout_process"),
        path("post/add", views.HazardReportCreate.as_view(), name='add-post'),
        path("posts/<user_name>", views.userPostList, name='userposts'),
        path("post/<int:hazardreport_id>", views.hazardreport, name="post"),
        path("search/", views.search_process, name="search_results"),
        path('map/', views.map, name="map"),
        path('media/', views.media, name="media"),
        path('report/', views.post_report, name='report'),
        path('update_status/', views.update_status, name='update_status'),
        path('process_new_report/', views.process_new_report, name='process_new_report'),
        re_path(r"^about(-\w*)?/?$", views.about, name="about"),  
]
