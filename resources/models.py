from django.db import models
from ckeditor.fields import RichTextField

class Resources(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = RichTextField()

    def __str__(self):
        return self.title