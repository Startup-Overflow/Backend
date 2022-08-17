from django.db import models
from ckeditor.fields import RichTextField


class BusinessIdea(models.Model):
    title = models.CharField(max_length=255)
    doi = models.CharField(max_length=255, unique=True) 
    url = models.CharField(max_length=255, unique=True)
    desc = RichTextField()

    def __str__(self): return self.title
    