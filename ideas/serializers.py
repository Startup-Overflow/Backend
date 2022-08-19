from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ideas.models import BusinessIdea

class BusinessIdeaSerializer(ModelSerializer):
    class Meta:
        model = BusinessIdea 
        fields = '__all__'
        
