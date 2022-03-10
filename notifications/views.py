from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from notifications.models import Notification
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['noti', 'post']

class NotificationView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = User.objects.get(username=request.user)
        noti = Notification.objects.filter(username=user)
        serializer = NotificationSerializer(noti, many=True)
        return Response(serializer.data)