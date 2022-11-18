from django.shortcuts import render


def get_home(request):
    """Get home page"""
    return render(request, 'home/index.html')


def get_about_page(request):
    """Get about page"""
    return render(request, 'home/about.html')
