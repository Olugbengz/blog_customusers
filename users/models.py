from typing import Any
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomBaseUserManager


# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=240)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = [
        'first_name',
        'last_name',
        'date_of_birth',
       ]
    
    objects = CustomBaseUserManager()
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(CustomUser, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return f"{self.user.first_name}'s profile."
