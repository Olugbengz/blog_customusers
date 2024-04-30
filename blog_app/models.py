from django.db import models
from django.conf import settings
from djrichtextfield.models import RichTextField




User = settings.AUTH_USER_MODEL


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blogCategory')
    title = models.CharField('Title', max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    body = RichTextField()
    author = models.ManyToManyField(User)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    blogpost_likes = models.ManyToManyField(User, related_name='blog_like')
    

    def num_of_likes(self):
        return self.blogpost_likes.count()

    def __str__(self):
        return f'{self.title} {self.author} {self.description} {self.created_at:%Y-%m-%d %H:%M}'
    


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='commentauthor')
    comment_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    comment_likes = models.ManyToManyField(User, related_name='comment_like')

    def num_of_likes(self):
        return self.comment_likes.count()
    
    def __str__(self):
        try:
            return 'Comment {} by {}'.format(self.comment_author.first_name, self.comment_text)
        except:
            return 'Anonymous: {} '.format(self.comment_text)

