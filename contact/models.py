import uuid
from django.db import models


class UserQuery(models.Model):
    """
    UserQuery Model for users interaction and feedback
    """
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=320, unique=False)
    comment = models.TextField()
    user_query_number = models.CharField(max_length=254,
                                         null=False,
                                         blank=False,
                                         default='')
    is_open = models.BooleanField(default=True)

    def _generate_user_query_number(self):
        """
        Private Method generates a random, unique user query number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the user query number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_query_number
