from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# When a user is saved do the function
# revierver is create profile
# if a user is created make a profile object to the user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# instance is the user
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() 