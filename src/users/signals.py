from django.contrib.auth.models import User
from django.db.models.base import post_save
from django.utils.translation.trans_real import receiver

from users.models import Profile, Location


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwrags):
    if created:
        profile_location = Location.objects.create()
        instance.location = profile_location
        instance.save()
