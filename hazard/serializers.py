from rest_framework import serializers
# Add import models for serialization
from .models import HazardReport, HazardReportComment
from django.contrib.auth.models import User

#Django’s serialization framework provides a mechanism for “translating” Django models into other formats. Usually these other formats will be 
#text-based and used for sending Django data over a wire, but it’s possible for a serializer to handle any format (text-based or not).
# Serialize models here from models.py 

# USER SERIALIZE 
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'pk')

# HAZARD REPORT COMMENT SERIALIZE 
class HazardReportCommentSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = HazardReportComment
        fields = ('content_text', 'pub_date', 'user')

# WHOLE HAZARD POST SERIALIZE 
class HazardReportSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    comments = HazardReportCommentSerializer(many=True)

    class Meta:
        model = HazardReport
        fields = ('title_text', 'content_text', 'pub_date', 'user', 'comments')
        depth = 2

# USER TO HAZARD REPORT SERIALIZE
class UserWithPostListSerializer(serializers.ModelSerializer):

    hazardposts = HazardReportSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'pk', 'hazardposts')
        depth = 3
