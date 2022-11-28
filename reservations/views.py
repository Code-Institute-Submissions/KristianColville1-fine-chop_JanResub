from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required
def create_booking(request):
    """
    Brings the user to the reservation page
    """
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=Booking())
        form.customer = request.user
        user_email = request.user.email
        messages.success(request,
                         f'Booking created! email sent to {user_email}')
        their_email = user_email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt')
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt')

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [their_email])
        form.save()

        return redirect(reverse('home'))
    form = BookingForm()

    context = {
        'form': form,
    }
    return render(request, 'reservations/booking.html', context)
