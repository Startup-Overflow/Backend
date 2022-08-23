from rest_framework.serializers import ModelSerializer
from resources.models import *

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resources
        fields = 'title'

class ResourceSerializerContent(ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = 'title'

class BookSerializerContent(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

