from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    """
    Profile model
    """
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=320, unique=True)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    default_phone_number = models.CharField(max_length=22,
                                            null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=90,
                                               null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=90,
                                               null=True,
                                               blank=True)
    default_town_or_city = models.CharField(max_length=55,
                                            null=True,
                                            blank=True)
    default_county = models.CharField(max_length=100, null=True, blank=True)
    default_postcode = models.CharField(max_length=18, null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True,
                                   blank=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for a user on sign up to connect everything
    together.
    """
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.email = instance.email
        user_profile.save()
