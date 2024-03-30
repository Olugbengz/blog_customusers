from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserProfile

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    # print(f"Sender is {sender} and Instance: {instance}")
    if created:
        UserProfile.objects.create(user=instance)
        

    