#Name: Mark
#Description: database model
#Usage: storing data to database
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# These are items for our database; Hazard Reports


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    title = models.CharField(max_length=45)

class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)

# hazard post Content and text lengths limit
class HazardReport(models.Model):
    pub_date = models.DateTimeField(auto_now_add = True)
    title_text = models.CharField(max_length=45)
    content_text = models.TextField()
    zipcode = models.CharField(max_length=5)
    location = models.CharField(max_length=50)

    user = models.ForeignKey(User, related_name="hazardposts",
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                             on_delete=models.CASCADE)
    status = models.ForeignKey(Status,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.title_text

# Date Field
# Hazard post comment Content and text lengths
class HazardReportComment(models.Model):
    pub_date = models.DateField(auto_now_add = True)
    content_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hazardreport = models.ForeignKey(HazardReport, related_name='comments',
                                 on_delete=models.CASCADE)