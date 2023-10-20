from django.contrib import admin
from .models import Category, Author, Blog, BlogPost

# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(BlogPost)