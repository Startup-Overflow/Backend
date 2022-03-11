from statistics import mode
from django.db import models
from django.contrib.auth.models import User

from posts.models import Posts

class Noti(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    noti = models.CharField(max_length=128, null=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return self.noti
