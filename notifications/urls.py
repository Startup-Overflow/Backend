from django.urls import path, include
from notifications.views import *

urlpatterns=[
    path('',NotificationView.as_view())
]