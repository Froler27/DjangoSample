from django.contrib import admin

# Register your models here.
from .models import Blog, User, Comment, Reply

admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Reply)