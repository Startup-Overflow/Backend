from django.urls import path
from questions.views import *

urlpatterns = [
    path('',QuestionsView.as_view()),
    path('<int:pk>/',QuestionsView.as_view()),
    path('answer/<int:pk>',AnswerView.as_view())
]