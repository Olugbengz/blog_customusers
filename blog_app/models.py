from django.db import models
from users.models import CustomUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Author(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Blog(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
