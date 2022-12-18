from django.shortcuts import render


def get_home(request):
    """
    Get home page
    """
    return render(request, 'home/index.html')


def get_about_page(request):
    """
    Get about page
    """
    return render(request, 'home/about.html')


def privacy_policy(request):
    """
    Privacy Policy page
    """
    return render(request, 'home/privacy_policy.html')


def terms_and_conditions(request):
    """
    Terms & conditions page
    """
    return render(request, 'home/terms_and_conditions.html')
