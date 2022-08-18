from rest_framework.serializers import ModelSerializer
from posts.models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        # fields = '__all__'
        exclude = ('desc', )

class PostDetailsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        # exclude = ('desc', )


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

