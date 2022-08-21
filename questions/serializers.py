from rest_framework.serializers import ModelSerializer
from questions.models import *

class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
