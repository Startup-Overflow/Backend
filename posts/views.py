from django.shortcuts import get_list_or_404
from posts.models import *
from posts.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from hashtag.models import TagFollow
from users.models import Follow, Hobbies, Interests, Skills
from noti.models import Noti
import time

class PostsViewToALL(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        posts = Posts.objects.get(id=pk)
        serializer = PostDetailsSerializer(posts, many=True)
        return Response(serializer.data)

# class PostsByCategory(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, category):
#         posts = Posts.objects.filter(category=category)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

class CommentViewToALL(APIView):
    permission_classes = (AllowAny,)

    def get(self, request,pk, format=None):
        posts = Posts.objects.get(id=pk)
        comments = Comments.objects.filter(posts=posts)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
  
  
class CommentView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        print("Comment")
        username = User.objects.get(username=request.user)
        posts = Posts.objects.get(id=request.data["id"])
        comment = request.data["addComment"]

        Comments.objects.create(
            username = username,
            posts = posts,
            comment = comment
        )
        curr_time = time.localtime()
        curr_clock = time.strftime("%H:%M:%S", curr_time)

        noti_to_user = posts.username
        msg = f"{username.first_name} {username.last_name} commented on {posts.title} at {curr_clock}"
        post = Posts.objects.get(id=posts.id)

        Noti.objects.create(
            username=noti_to_user,
            noti = msg,
            post=post
        )

        return Response({"Comment":comment})

class PostsViewSet(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, catagory=None, format=None):
        followings = Follow.objects.filter(username=request.user)
        post = Posts.objects.filter(username=request.user)
                
        posts = Posts.objects.all()
        # filter(
        #     username__in=[i.following.username for i in followings]
        #     +[i.username for i in post]
        # ).filter(catagory=catagory)

        print([i for i in posts])
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        username = User.objects.filter(username=request.user).first()
        title = request.data["title"]
        desc = request.data["desc"]
        short_desc = request.data["shrtdesc"]
        catagory = request.data["catagory"]
        hasht = Hashtag.objects.filter(name__in=request.data["hashtag"])
        a = Posts.objects.create(
            username = username,
            title = title,
            desc = desc,
            catagory = catagory,
            short_desc = short_desc,
        )
        a.hashtag.set(hasht)
        a.save()

        return Response({"Response":"Success"})

class PostByTagView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, catagory=None, format=None):
        hashtags = TagFollow.objects.filter(follower=request.user).values('name')
        hobbies = Hobbies.objects.filter(username=request.user)
        skills = Skills.objects.filter(username=request.user)
        interests = Interests.objects.filter(username=request.user)
        posts2 = Posts.objects.filter(
           hashtag__in=[i['name'] for i in hashtags]
           +[i.name.name for i in hobbies]
           +[i.name.name for i in interests]
           +[i.name.name for i in skills]
        ).filter(catagory=catagory).distinct()

        serializer = PostSerializer(posts2, many=True)
        return Response(serializer.data)


class ViewsByHashtag(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, requests, hashtag):
        tags = Hashtag.objects.filter(name=hashtag)
        post = Posts.objects.filter(hashtag__in = [i for i in tags])
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

class MyArticleView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get(self, requests, catagory):
        posts = Posts.objects.filter(username=requests.user).filter(catagory=catagory)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


#
# class PostsViewSet(APIView):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
    
#     def get(self, request, pk=None):
#         if pk is None:
#             posts = Posts.objects.all()
#             serializer = PostSerializer(posts, many=True)
#             return Response(serializer.data)
#         else:
#             posts = Posts.objects.filter(id=pk)
#             serializer = PostSerializer(posts, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         username = User.objects.get(username=request.user)
#         hashtag = Hashtag.objects.filter(hashtag__in=request.data["hashtag"])
#         posts = Posts.objects.create(
#             username = username,
#             title = request.data["title"],
#             desc = request.data["desc"],
#         )
#         posts.hashtag.set(hashtag)
#         posts.save()
#         return Response({"Response":"Post Created"},status=status.HTTP_201_CREATED)