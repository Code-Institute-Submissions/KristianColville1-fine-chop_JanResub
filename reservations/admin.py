from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin Model for Table arrangements
    """
    list_display = ('pk', 'table_number', 'seating_amount',
                    'disabled_friendly')
    list_filter = ('seating_amount', 'disabled_friendly')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin Model for Bookings
    """
    list_display = ('pk', 'customer', 'booked_table', 'guest_amount', 'date',
                    'time')
    search_fields = ['pk', 'customer__username']
    list_filter = ('time', ('date', DateRangeFilter), 'booked_table')
