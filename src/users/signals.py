from django.contrib.auth.models import User
from django.db.models.base import post_save
from django.utils.translation.trans_real import receiver

from users.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
