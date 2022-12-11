from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

ROLE_CHOICES = (
    (1, "CUSTOMER"),
    (2, "STAFF"),
    (3, "MARKETER"),
    (4, "ADMIN"),
)


class Role(models.Model):
    """
    Assigns a default role to the user profile
    can be changed in admin to allow staff and
    extended team functionalities.
    Abstract class.
    """
    user_role = models.IntegerField(choices=ROLE_CHOICES, default=1)
    title = models.CharField(max_length=200, blank=True, null=True)
    duties = models.TextField(max_length=1000, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'User Roles'
        abstract = True

    def __str__(self):
        """
        Returns the name of the user role
        """
        return f'{self.role}'


class Address(models.Model):
    """
    Stores the users information for their address.
    Abstract class.
    """
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
        verbose_name_plural = 'User Address'
        abstract = True

    def __str__(self):
        """
        Returns the user phone number and
        first line of their address
        """
        return f'{self.default_phone_number} {self.default_street_address1}'


class Profile(Role, Address):
    """
    Profile model Mixin
    """
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=320, unique=True)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
