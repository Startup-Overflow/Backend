from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from users.models import Profile

days = [("Sun","Sunday"), ("Mon","Monday"), ("Tue","Tuesday"), ("Wed","Wednesday"), ("Thu","Thursday"), ("Fri","Friday"), ("Sat","Saturday")]

"""
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=250,null=True)
    mobile_no = models.CharField(max_length=15,null=True)
    entre = models.BooleanField(default=False)
    mentor = models.BooleanField(default=False)
    investor = models.BooleanField(default=False)
    incubator = models.BooleanField(default=False)
    partner = models.BooleanField(default=False)
    job_seaker = models.BooleanField(default=False)

    def __str__(self):
        return self.username.username
"""
    
# class RatingReview(models.Model):
#     mentors = models.ForeignKey(User, related_name='username', on_delete=models.CASCADE)
#     users = models.ForeignKey(User, on_delete=models.CASCADE)
#     review = models.CharField(max_length=250,null=True)
#     rating = models.IntegerField(default=0)

#     def save(self, *args, **kwargs):
#         if Profile.objects.get(username=self.mentor).mentor:
#             super(RatingReview, self).save(*args, **kwargs)
#         else:
#             raise ValueError("User is not a mentor")


class Available(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    day = models.CharField(max_length=3, choices=days, default=datetime.today().strftime('%A'))
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return self.username.username

class Book(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    available = models.ForeignKey(Available, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return self.username.username
    
    # def save(self, *args, **kwargs):
    #     # print(self.available.username, type(self.available.username))
    #     # print(Available.objects.get(username=self.available.username).start_time > self.start_time)
    #     if Available.objects.get(username=self.available.username).start_time > self.start_time or Available.objects.get(username=self.available.username).end_time < self.end_time:
    # #     if self.start_time > Available.objects.get(username=self.username).start_time or self.end_time < Available.objects.get(username=self.username).start_time:
    #         raise ValueError("Mentor is not available at this time")
    #     super(Book, self).save(*args, **kwargs)
