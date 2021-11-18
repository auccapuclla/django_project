from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #saved user, send signal to receiver
def create_profile(sender, instance, created, **kwargs): #receiver is create_profile function
    if created: #all arguments in create_profile were passed to from post_save
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User) #save profile
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()