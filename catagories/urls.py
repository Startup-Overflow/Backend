from django.urls import path
from catagories.views import Learn

urlpatterns = [
    path('', Learn.as_view() ),
    path('<int:id>/', Learn.as_view() ),
]