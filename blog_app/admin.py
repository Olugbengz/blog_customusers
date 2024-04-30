from django.contrib import admin
from .models import Category, Blog, BlogPost, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(BlogPost)
admin.site.register(Comment)
