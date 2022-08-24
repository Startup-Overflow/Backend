from django.db import models
from django.contrib.auth.models import User
from hashtag.models import Hashtag
from ckeditor.fields import RichTextField

class Questions(models.Model):
    username = models.ForeignKey(User, to_field="username",on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140, null=True)
    desc = RichTextField(default=None)
    # attachment = models.FileField(upload_to='posts/', null=True)
    hashtag = models.ManyToManyField(Hashtag, related_name="questionhashtag")
    answer = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Answer(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True, related_name="question")
    title = models.CharField(max_length=140, null=True)
    desc = models.TextField(null=True)
    # attachment = models.FileField(upload_to='posts/', null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        post = Questions.objects.get(id=self.question.id)
        post.answer = post.answer+1
        post.save()
        super(Answer, self).save(*args, **kwargs)


