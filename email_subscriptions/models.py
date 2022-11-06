from django.db import models


class Subscriber(models.Model):
    """ Subscriber Model """
    email = models.CharField(max_length=320, unique=True)
    name = models.CharField(max_length=120, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.email
