from rest_framework.serializers import ModelSerializer
from resources.models import Resources

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'