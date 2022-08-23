from django.db import models
from ckeditor.fields import RichTextField

class Resources(models.Model):
    title = models.CharField(max_length=255, unique=True)
    desc = RichTextField()
    # image = models.ImageField(max_length=255, blank=True, upload_to='resources/')

    def __str__(self):
        return self.title

class Courses(models.Model):
    title = models.CharField(max_length=255, unique=True)
    desc = RichTextField()

class Books(models.Model):
    title = models.CharField(max_length=255, unique=True)
    desc = RichTextField()
