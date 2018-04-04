from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField
from .models import HazardReport, HazardReportComment
import sys
