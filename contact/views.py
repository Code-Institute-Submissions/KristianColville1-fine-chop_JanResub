from django.shortcuts import render


def contact_us(request):
    """
    Contact us page
    """
    return render(request, 'contact/contact_us.html')


def careers(request):
    """
    Career page
    """
    return render(request, 'contact/careers.html')
