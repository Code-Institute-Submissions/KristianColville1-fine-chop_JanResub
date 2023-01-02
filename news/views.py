from django.shortcuts import render, redirect
from django.core.validators import validate_email
from .decorators import user_is_superuser
from django.core.exceptions import ValidationError
from profiles.models import Profile
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import SubscribedUsers
from .forms import NewsletterForm


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(
                request, "You must type legit name and email to subscribe \
                to a Newsletter")
            return redirect("/")

        if Profile.objects.filter(email=email).first():
            messages.error(
                request, "Your already registered with us!")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request,
                           f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(
            request,
            f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))


@user_is_superuser
def news(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject,
                                email_message,
                                f"FineChop <{request.user.email}>",
                                bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent successfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join(
        [active.email for active in SubscribedUsers.objects.all()])
    return render(request=request,
                  template_name='main/newsletter.html',
                  context={'form': form})
