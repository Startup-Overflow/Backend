from django.urls import path
from ideas.views import BusinessIdeaView


urlpatterns = [
    path('', BusinessIdeaView.as_view()),
]