
from django import forms
from .models import Booking, Table


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    Form to create a reservation for booking a table at FineChop
    """

    class Meta:
        model = Booking
        fields = [
            'guest_amount', 'time', 'date', 'email',
            'phone_number'
        ]
        widgets = {
            'date': DateInput(),
        }

    field_order = ['email', 'phone_number', ...]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'guest_amount': 'Number of Guests',
            'booked_table': 'Table Number',
            'time': 'Times Available',
            'date': 'Dates Available',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
