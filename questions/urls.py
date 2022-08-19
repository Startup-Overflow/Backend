from django.urls import path
from questions.views import QuestionsView

urlpatterns = [
    path('',QuestionsView.as_view()),
    path('<int:pk>/',QuestionsView.as_view())
]