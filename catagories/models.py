from django.db import models
from django.contrib.auth.models import User

def superuser(): return User.objects.filter(is_superuser=True)

class Catagory(models.Model):
    username = models.ForeignKey(User, on_delete=superuser, null=True)
    name = models.CharField(max_length=12, unique=True)
    desc = models.TextField(null=True)
    # follower = models.ManyToManyField(User, related_name="tagfollower")
    
    def __str__(self):
        return self.name
