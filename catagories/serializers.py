from dataclasses import field
from rest_framework.serializers import ModelSerializer
from catagories.models import Catagory

class LearnSerializer(ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'