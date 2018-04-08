from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField
from .models import HazardReport, HazardReportComment
import sys

# User sign up form ( username , email , password)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    if sys.argv[1] != 'test':
        captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Hazard Report form ( title , context )
class HazardReportForm(forms.ModelForm):

    class Meta:
        model = HazardReport
        fields = ['title_text', 'content_text', 'zipcode', 'location']

# Hazard report comment form (comment)
class HazardReportCommentForm(forms.ModelForm):

    class Meta:
        model = HazardReportComment
        fields = ['content_text']
