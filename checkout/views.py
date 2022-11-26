from django.shortcuts import render


def get_checkout(request):
    """Get checkout page"""
    return render(request, 'checkout/checkout.html')
