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

class CoursesHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id, *args, **kwargs):
        if id is not None:
            course = Courses.objects.get(id=id)
            serializer = ResourceSerializerContent(course)
            return Response(serializer.data)
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
        
class BooksHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id, *args, **kwargs):
        if id is not None:
            book = Books.objects.get(id=id)
            serializer = BookSerializerContent(book)
            return Response(serializer.data)
        book = Books.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
         