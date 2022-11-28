import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
"""Reservations Models for booking tables at FineChop"""

# Choice fields

BOOKING_TIMES = (
    (0, "11:15AM - 12:00PM"),
    (1, "12:15PM - 1:45PM"),
    (2, "1:15PM - 3:45PM"),
    (3, "2:15PM - 4:45PM"),
    (4, "3:15PM - 5:45PM"),
    (5, "4:15PM - 6:45PM"),
    (6, "5:15PM - 7:45PM"),
    (7, "6:15PM - 9:00PM"),
    (8, "7:15PM - 9:45PM"),
)

TABLE_NUMBER = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
)


class Table(models.Model):
    """
    Table model for seating amount and
    if the table is disabled friendly
    """

    class Meta:
        verbose_name_plural = 'Tables'

    table_number = models.IntegerField(choices=TABLE_NUMBER, default=1)
    seating_amount = models.IntegerField(default=2)
    disabled_friendly = models.BooleanField(default=True)

    def __str__(self):
        return str(self.table_number)


class Booking(models.Model):
    """
    Model to create a booking
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="booking_customer", null=True)
    booked_table = models.ForeignKey(Table,
                                     on_delete=models.CASCADE,
                                     related_name="booking_table", null=True)
    guest_amount = models.IntegerField(
        default=2, validators=[MinValueValidator(1),
                               MaxValueValidator(16)])
    date = models.DateField(null=True, blank=True)
    time = models.IntegerField(choices=BOOKING_TIMES, default=1)
    email = models.EmailField(max_length=254, blank=False, null=True)
    phone_number = models.CharField(max_length=22, blank=False, null=True)

    class Meta:
        """
        Order of Bookings by date and time
        """
        ordering = ['date', 'time']

    def _generate_order_number(self):
        """
        Private Method generates a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the order number
        if it hasn't been set already for the booking.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
