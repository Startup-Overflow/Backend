from django.contrib import admin
from questions.models import Questions, Answer

admin.site.register([Questions, Answer])


