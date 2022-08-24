from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from hashtag.models import *
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class HashtagSerializer(ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['name','desc']

class TagFollowSerializer(ModelSerializer):
    class Meta:
        model = TagFollow
        fields = ['name','follower']
