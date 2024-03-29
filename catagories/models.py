from django.db import models
from django.contrib.auth.models import User

def superuser(): return User.objects.filter(is_superuser=True)

class Catagory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
