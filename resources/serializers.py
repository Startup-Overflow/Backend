from rest_framework.serializers import ModelSerializer
from resources.models import *

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resources
        fields = ('title')

class ResourceSerializerContent(ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'

class SchemeCourseBookEventSerializer(ModelSerializer):
    class Meta:
        model = SchemeCourseBookEvent
        fields = ('title', 'desc')
