from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a profile when a new user is created"""
    if created:
        Profile.objects.create(
            user=instance,
            full_name=instance.full_name,
            avatar_url=instance.avatar_url
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the profile when user is saved"""
    if hasattr(instance, 'profile'):
        instance.profile.full_name = instance.full_name
        instance.profile.avatar_url = instance.avatar_url
        instance.profile.save()
