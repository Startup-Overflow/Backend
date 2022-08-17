from django.shortcuts import render
from rest_framework.views import APIView
from resources.models import Resources
from resources.serializers import ResourceSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

class ResourcesHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        resources = Resources.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)
