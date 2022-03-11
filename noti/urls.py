from django.urls import path, include
from noti.views import *

urlpatterns=[
    path('',NotiView.as_view())
]