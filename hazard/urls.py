from django.urls import path
from . import views

# APP NAME AND URL PATHING / ROUTES

#  (path  link/url   ,  (views.py).Class/Definition  ,  name)
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
        path("about/", views.about, name="about"),
        path('map/', views.map, name="map"),
]
