from asyncore import read
from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer, StringRelatedField
from django.contrib.auth.models import User
from users.models import *

class UserTypeSerializer(ModelSerializer):
    class Meta:
        model = UsersType
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('username',)

class UserSerializer(ModelSerializer):    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]

class FollowSerializer(ModelSerializer):
    class Meta:
        model = Follow
        fields = ['following']
        
class HobbiesSerializer(ModelSerializer):
    class Meta:
        model = Hobbies
        fields = '__all__'

class InterestsSerializer(ModelSerializer):
    class Meta:
        model = Interests
        fields = '__all__'
    
class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'