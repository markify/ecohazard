from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
# ---- login/logout import ----
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# ---- forms.py, models.py import ----
from .forms import UserForm, HazardReportForm, HazardReportCommentForm
from .models import HazardReport, HazardReportComment
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# ---- rest import ----
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# ---- serializer import ----
from .serializers import HazardReportSerializer, UserWithPostListSerializer


# ---- ABOUT PAGES ----

def about(request, extra=None):
    switcher = {
        '-ali': 'hazard/about/about-ali.html',
        '-cameron': 'hazard/about/about-cameron.html',
        '-girish': 'hazard/about/about-girish.html',
        '-humeston': 'hazard/about/about-humeston.html',
        '-larsen': 'hazard/about/about-larsen.html',
        '-mark': 'hazard/about/about-mark.html',
        '-sutherland': 'hazard/about/about-sutherland.html'
    }
    if extra:
        return render(request, switcher.get(extra, 'hazard/about.html'))
    return render(request, 'hazard/about.html')

# ---- MAP VIEW ----
def map(request):
    return render(request, 'hazard/map.html')
    


# RENDERS THE INDEX HOME PAGE
def index(request):
    last_post_list = HazardReport.objects.order_by("-pub_date")[::-1]
    # render number of current post in the index page ie home page <-

    context = {
            'list': current_post_list,
            'num_pages': num_pages
    }
    return render(request, "hazard/index.html", context)

# USER HAS LOGGIN WITH USER AUTHENTHICATION REDIRECT TO INDEX
def login_process(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('ecohazards:index')

    return redirect('ecohazards:index')

# RENDERS THE HOME PAGE WHEN USER HAS LOGGED OUT
# THEN REDIRECTS TO INDEX PAGE
def logout_process(request):
    if request.user is not None:
        logout(request)
    return redirect('ecohazards:index')


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

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_id = request.user.id
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

    post_list = HazardReport.objects.filter(user__id__exact=\
            user_id).order_by('-pub_date')[::-1]
    # render the number of views of my post 5
 
    context = {
            'list': current_post_list,
            'num_pages': num_pages,
            'user_name': user_name
    }
    return render(request, "hazard/user_post_list.html", context)

# ---- Renders hazard CONTEXT of the post inside the report ----
def hazardreport(request, hazardreport_id):
    form_class = HazardReportCommentForm
    if request.method == 'POST':
        form = form_class(request.POST)
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
    comments = HazardReportComment.objects.filter(hazardreport__id__exact=\
            hazardreport_id).order_by('-pub_date')
    context = {'hazardreport': hazardreport, 'comments': comments, 'form': form}
    return render(request, template_name, context)

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
