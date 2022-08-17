from django.contrib import admin

# Register your models here.
from mentors.models import Available, Book

admin.site.register([Available, Book])