from django.shortcuts import render
from ideas.models import BusinessIdea
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from ideas.serializers import BusinessIdeaSerializer
from rest_framework.response import Response

class BusinessIdeaView(APIView):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    
    def get(self, requests, format=None, *args, **kwargs):
        idea = BusinessIdea.objects.all()
        serializer = BusinessIdeaSerializer(idea, many=True)
        return Response(serializer.data)
