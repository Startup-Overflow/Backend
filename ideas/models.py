from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

def superuser(): return User.objects.filter(is_superuser=True)

class BusinessIdea(models.Model):
    user = models.ForeignKey(User, on_delete=superuser, null=True)
    title = models.CharField(max_length=255)
    doi = models.CharField(max_length=255, unique=True) 
    url = models.CharField(max_length=255, unique=True)
    desc = RichTextField()

    def __str__(self): return self.title
