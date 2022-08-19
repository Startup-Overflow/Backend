from django.shortcuts import render
from rest_framework.views import APIView
from resources.models import Resources
from resources.serializers import ResourceSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *


class ResourcesHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            resources = Resources.objects.exclude(id__in=[14, 15, 16 ]) #all()
            serializer = ResourceSerializer(resources, many=True)
        else:
            resources = Resources.objects.get(id=pk)
            serializer = ResourceSerializer(resources)
        return Response(serializer.data)

