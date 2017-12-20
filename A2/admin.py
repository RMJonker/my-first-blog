from django.contrib import admin
from .models import Post
from .models import Task

admin.site.register(Post)
admin.site.register(Task)