from django.contrib import admin

# Register your models here.

from .models import Course, Lesson, Comment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)