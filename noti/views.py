from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from noti.models import Noti
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class NotiSerializer(ModelSerializer):
    class Meta:
        model = Noti
        fields = ['noti', 'post']

class NotiView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = User.objects.get(username=request.user)
        noti = Noti.objects.filter(username=user)
        serializer = NotiSerializer(noti, many=True)
        return Response(serializer.data)