from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactUsForm


def contact_us(request):
    """
    Contact us page
    """

    if request.method == 'POST':
        print('here')
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'comment': request.POST['comment'],
        }

        contact_form = ContactUsForm(form_data)
        if contact_form.is_valid():
            form = contact_form.save()
            pid = form.user_query_number
            messages.info(request, ('Thanks for for your query'
                                    'Please check your email.'
                                    f'Your query number is {pid}'))
            their_email = form.email
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'form': form})
            body = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'form': form})
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                      [their_email])
            return render(redirect(''))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    context = {'contact_form': ContactUsForm}
    return render(request, 'contact/contact_us.html', context)


def careers(request):
    """
    Career page
    """
    return render(request, 'contact/careers.html')
