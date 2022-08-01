import imp
from django.db import models
from django.contrib.auth.models import User
from hashtag.models import Hashtag

class Job(models.Model):
    company = models.ManyToManyField(User, related_name='company', null=True)
    jobseaker = models.ManyToManyField(User, related_name='jobseaker', null=True)
    title = models.CharField(max_length=128, null=True)
    desc = models.TextField(null=True)
    hashtag = models.ManyToManyField(Hashtag, related_name='hashtag', null=True)