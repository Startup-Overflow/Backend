from django.shortcuts import render
from rest_framework.views import APIView
from resources.models import *
from resources.serializers import *
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *


class ResourcesHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            resources = Resources.objects.all()
            serializer = ResourceSerializer(resources, many=True)
        else:
            resources = Resources.objects.get(id=pk)
            serializer = ResourceSerializer(resources)
        return Response(serializer.data)

class SchemeCourseBookEventHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id, *args, **kwargs):
        if id is not None:
            scbe = SchemeCourseBookEvent.objects.get(id=id)
            serializer = ResourceSerializerContent(scbe)
            return Response(serializer.data)
        scbe = SchemeCourseBookEvent.objects.all()
        serializer = SchemeCourseBookEventSerializer(scbe, many=True)
        return Response(serializer.data)
         