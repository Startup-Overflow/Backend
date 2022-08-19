from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from hashtag.models import Hashtag

def superuser(): return User.objects.filter(is_superuser=True)

class BusinessIdea(models.Model):
    user = models.ForeignKey(User, on_delete=superuser, null=True)
    title = models.CharField(max_length=255)
    doi = models.CharField(max_length=255, unique=True, default=None) 
    url = models.CharField(max_length=255, unique=True, default=None)
    desc = RichTextField()
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE, null=True)

    def __str__(self): return self.title
