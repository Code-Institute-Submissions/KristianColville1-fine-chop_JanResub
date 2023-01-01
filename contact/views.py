from django.shortcuts import render
from .forms import ContactUsForm


def contact_us(request):
    """
    Contact us page
    """
    # if request.method == 'POST':
        
    context = {
        'contact_form': ContactUsForm
    }
    return render(request, 'contact/contact_us.html', context)


def careers(request):
    """
    Career page
    """
    return render(request, 'contact/careers.html')
