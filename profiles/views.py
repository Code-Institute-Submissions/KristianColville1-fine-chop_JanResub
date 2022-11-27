from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

    profile_form = ProfileForm(instance=profile)
    orders = Order.objects.filter(user_profile=profile)

    template = 'profiles/profile.html'
    context = {
        'profile_form': profile_form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (f'This is a past confirmation for order number {order_number}. '
         'A confirmation email was sent on the order date.'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
