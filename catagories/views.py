from django.shortcuts import render
from rest_framework.views import APIView
from catagories.models import Catagory
from catagories.serializers import LearnSerializer
from rest_framework.response import Response
from posts.models import Posts
from posts.serializers import PostSerializer
from rest_framework.permissions import *

class Learn(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, id=None):
        if id is None:
            catagory = Catagory.objects.exclude(id__in=[14, 15, 16 ])
            serializer = LearnSerializer(catagory, many=True)
            return Response(serializer.data)
        else:
            print(id)
            catagory = Catagory.objects.get(id=id)
            post = Posts.objects.filter(catagory=catagory)
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data)
