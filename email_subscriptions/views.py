from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Subscriber
from django.core.mail import send_mail
from django.conf import settings
import re


def index(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subscribedUser = Subscriber()
        subscribedUser.email = email
        subscribedUser.name = name
        subscribedUser.save()
        subject = 'FineChop Newsletter Subscription'
        message = 'Hello ' + name + """,

        Thanks for subscribing with us. You will now get notifications on
        the latest offers, meals and promotions from FineChop.
        Please do not reply on this email."""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            email,
        ]
        send_mail(subject, message, email_from, recipient_list)
        re = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return re
    return redirect(request.META.get('HTTP_REFERER', '/'))


def validate_email(request):
    email = request.POST.get("email", None)
    if email is None:
        re = JsonResponse({'msg': 'Email is required.'})
    elif Subscriber.objects.filter(email=email):
        re = JsonResponse({'msg': 'Your already subscribed'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",
                      email):
        re = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        re = JsonResponse({'msg': ''})
    return redirect(request.META.get('HTTP_REFERER', '/'), re)
