#Name: CSC Team 07
#Description: this is where the views are created 
#Usage: acts as a view for rendering the web
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
# ---- login/logout import ----
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# ---- forms.py, models.py import ----
from .forms import UserForm, HazardReportForm, HazardReportCommentForm, CategoryForm
from .models import HazardReport, HazardReportComment, Category, Status
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# ---- serializer import ----
from .serializers import HazardReportSerializer, UserWithPostListSerializer

from django.utils.timezone import now
from django.db import models
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

from django.shortcuts import render_to_response
from django.template import RequestContext

# NO ROUTES FOUND PAGES

def handler404(request, exception):
    context = RequestContext(request)
    err_code = 404
    response = render_to_response('hazard/404.html', {"code":err_code}, context)
    response.status_code = 404
    return response

def handler500(request, exception):
    context = RequestContext(request)
    err_code = 500
    response = render_to_response('hazard/500.html', {"code":err_code}, context)
    response.status_code = 500
    return response

# ABOUT PAGE

def about(request, extra=None):
    return render(request, 'hazard/about.html')

# HAZARD TYPES 

class HazardTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'hazard_types'

# RENDERS THE POST THAT IS CURRENT AND CREATE PAGINATION
def get_paginator(request, list_of_items, count_per_page):
    """ Takes request, list of items and count of items per page.

    Returns correct list of items for current page, and
    a number of the page
    """
    paginator = Paginator(list_of_items, count_per_page)
    page = request.GET.get('page')
    try:
        current_post_list = paginator.page(page)
    except PageNotAnInteger:
        current_post_list = paginator.page(1)
    except EmptyPage:
        current_post_list = paginator.page(paginator.num_pages)
    num_pages = range(1, paginator.num_pages + 1)
    return current_post_list, num_pages


# RENDERS THE INDEX HOME PAGE
def index(request):
    groups = request.user.groups.all().values_list('name', flat=True)
    if "EnvironmentalManager" in groups:
        is_manager = 1
    else:
        is_manager = 0
    statuses = Status.objects.all()
    last_post_list = HazardReport.objects.order_by("-pub_date")[::0]
    # render number of current post in the index page ie home page <-
    current_post_list, num_pages = get_paginator(request, last_post_list, 10)
    context = {
        'list': current_post_list,
        'num_pages': num_pages,
        'statuses': statuses,
        'is_manager': is_manager
    }
    return render(request, "hazard/index.html", context)


# USER HAS LOGIN WITH USER AUTHENTHICATION REDIRECT TO INDEX

def login_process(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('ecohazards:index')
        else:
            messages.error(request, 'Login Failed : User name or password incorrect')
            return redirect('ecohazards:index')
    else:
        form = AuthenticationForm()
    return render(request, 'ecohazards:index', {'form': form})


# RENDERS THE HOME PAGE WHEN USER HAS LOGGED OUT
# THEN REDIRECTS TO INDEX PAGE
def logout_process(request):
    if request.user is not None:
        logout(request)
    return redirect('ecohazards:index')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# ---- RENDERS ALL THE SEARCH REQUEST , SEARCH QUERY ----
def search_process(request):
    search = request.GET['q']
    if(is_number(search) and float(search) < 0):
        # search_list=HazardReport.objects.none
        current_post_list, num_pages = HazardReport.objects.none(),0

    else:
        search_list = HazardReport.objects. \
            filter(Q(title_text__icontains=search)
                   | Q(content_text__icontains=search)
                   | Q(pub_date__icontains=search)
                   | Q(zipcode__icontains=search)
                   | Q(location__icontains=search))
    # number of search results 6
        current_post_list, num_pages = get_paginator(request, search_list, 6)
    context = {
        'list': current_post_list,
        'num_pages': num_pages,
        'search': search
    }
    return render(request, 'hazard/search_results.html', context)


# ---- RENDERS THE SIGNUP/REGISTRATION FORM ----
class UserFormView(View):
    form_class = UserForm
    template_name = "hazard/registration_form.html"

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # don't add to db yet
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # return User object if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('ecohazards:index')

        return render(request, self.template_name, {'form': form})


# ---- CREATE NEW HAZARD REPORT VIEW ----
class HazardReportCreate(CreateView):
    """Creates new post """
    form_class = HazardReportForm
    template_name = "hazard/hazardreport_form.html"
    categories = Category.objects.all()

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'categories': self.categories})

    def post(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_id = request.user.id
            new_post.status_id = 1
            new_post.save()
        return redirect('ecohazards:post', hazardreport_id=new_post.id)


#  ---- RENDERS THE POST OF THE USER LOGGED IN ----
def userPostList(request, user_name):
    """Returns render of all posts of a specific user"""
    if user_name == "my":
        user_id = request.user.id
    else:
        user_of_post = get_object_or_404(User, username=user_name)
        user_id = user_of_post.id

    post_list = HazardReport.objects.filter(user__id__exact= \
                                                user_id).order_by('-pub_date')[::0]
    # render the number of views of my post 5
    current_post_list, num_pages = get_paginator(request, post_list, 5)
    context = {
        'list': current_post_list,
        'num_pages': num_pages,
        'user_name': user_name
    }
    return render(request, "hazard/user_post_list.html", context)

# ---- RENDERS New Dashboard for CityManager ---- #
def CityManagerDashboard(request):
    data = HazardReport.objects.all()
    return render(request, 'hazard/dashboard.html', {'data': data})


# ---- Renders hazard CONTEXT of the post inside the report ----
def hazardreport(request, hazardreport_id):
    form_class = HazardReportCommentForm
    statuses = Status.objects.all()
    groups = request.user.groups.all().values_list('name', flat=True)
    if "EnvironmentalManager" in groups:
        is_manager = 1
    else:
        is_manager = 0

    if request.method == 'POST':
        form = form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user_id = request.user.id
            new_comment.hazardreport_id = hazardreport_id
            new_comment.save()
        return redirect('ecohazards:post', hazardreport_id=hazardreport_id)
    form = form_class(None)
    template_name = "hazard/HazardReport.html"
    hazardreport_id = hazardreport_id
    hazardreport = get_object_or_404(HazardReport, pk=hazardreport_id)
    comments = HazardReportComment.objects.filter(hazardreport__id__exact= \
                                                      hazardreport_id).order_by('-pub_date')
    context = {'hazardreport': hazardreport, 'comments': comments, 'form': form, 'statuses': statuses, 'is_manager': is_manager}
    return render(request, template_name, context)


# --- Updates hazard status via AJAX ----
def update_status(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = HazardReport.objects.get(pk=request.POST['hazard_report_id'])
            obj.status_id = request.POST['status_id']
            obj.save()
            return JsonResponse({'status': 'Success', 'msg': 'Status updated successfully'});
        except MyModel.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'});
    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'});


# ---- hazard Post API ----

class AllHazardReportAPI(APIView):
    """ Lists all objects of hazardreport class to api """

    def get(self, request):
        hazardposts = HazardReport.objects.all()
        serializer = HazardReportSerializer(hazardposts, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# ---- GET METHOD FOR ALL HAZARD POST ----

@api_view(['GET'])
def hazardreportAPI(request, hazardreport_id):
    hazardreport = get_object_or_404(HazardReport, pk=hazardreport_id)
    serializer = HazardReportSerializer(hazardreport, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def userHazardPostListAPI(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserWithPostListSerializer(user)
    return Response(serializer.data)
