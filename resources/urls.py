from django.urls import path, include
from resources.views import *
urlpatterns = [
    path('', ResourcesHandler.as_view(), name='resources'),
    path('<pk:int>', ResourcesHandler.as_view(), name='resourcesid'),
]