from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Posts 

class HomeView(ListView):
    model = Posts
    template_name = "home.html"    