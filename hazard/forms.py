#Name: CSC Team 07
#Description: User forms , hazard forms are created
#Usage: Create the data process
from django.contrib.auth.models import User
from django import forms
from ***REMOVED***.fields import ReCaptchaField
from ***REMOVED***.widgets import ReCaptchaWidget
from .models import HazardReport, HazardReportComment, Category
import sys

# User sign up form ( username , email , password)
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username' }))
    email = forms.CharField(max_length=45, help_text='100 characters max.',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(max_length=45,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Hazard Report form ( title , context )

class HazardReportForm(forms.ModelForm):
    title_text = forms.CharField(max_length=44,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title of report'}))
    content_text = forms.CharField(max_length=240,widget=forms.Textarea(attrs={'class':'form-control','rows': 5, 'cols': 49}))
    zipcode = forms.CharField(max_length=5,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}))
    location = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}))


    class Meta:
        model = HazardReport
        fields = ['category', 'title_text', 'content_text', 'zipcode', 'location']

# Hazard report comment form (comment)
class HazardReportCommentForm(forms.ModelForm):
    content_text = forms.CharField(max_length=240,widget=forms.Textarea(attrs={'class':'form-control','rows': 5, 'cols': 49}))
    class Meta:
        model = HazardReportComment
        fields = ['content_text']

class CategoryForm(forms.Form):
    class Meta:
        model = Category
        categories = forms.ModelChoiceField(queryset=Category.objects.all().order_by('id'))