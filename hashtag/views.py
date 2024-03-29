from urllib import response
from hashtag.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.authentication import TokenAuthentication
import hashlib
from django.db.utils import IntegrityError
from hashtag.serializers import *

class HashTagFollow(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, requests):
        username=requests.user
        name = requests.data["name"]
        desc = requests.data["desc"]

        h = Hashtag.objects.create(
            username=username,
            name=name,
            desc=desc
        )
        h.save()

        return Response({"Response":"Success"})

class TagView(APIView):
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, pk=None, format=None):
        if pk is None:
            hashtag = Hashtag.objects.all()
            serializer = HashtagSerializer(hashtag, many=True)
            return Response(serializer.data)
        else:
            hashtag = Hashtag.objects.get(name=pk)
            # print(hashtag.name)
            followers = TagFollow.objects. filter(name=hashtag) #.values('follower')
            # print(followers)
            followers = [i['follower'] for i in followers.values('follower')]
            print(followers)
            # print(TagFollow.objects.filter(id__in=[i['id'] for i in followers]))
            users = User.objects.filter(id__in=followers)
            print([i.username for i in users])
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        name = Hashtag.objects.filter(name=request.data['hashtag'])
        print(name)
        if not name:
            return Response({"Response":"Hashtag Does Not Exist"})
        follower = User.objects.filter(username=request.user)
        hashvalue = str(follower)+str(name)
        print(hashvalue)
        checkunique = hashlib.md5(hashvalue.encode())
        print(checkunique.hexdigest())
        try:
            a = TagFollow.objects.create(checkunique=checkunique.hexdigest())
            a.follower.set(follower)
            a.name.set(name)
            a.save()
            return Response({"Response":"Following"})
        except IntegrityError:
            return Response({"Response":"Already Followed"})

