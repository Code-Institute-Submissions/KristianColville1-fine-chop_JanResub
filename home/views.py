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
    lines = [
        line.strip()
        for line in open('home/static/home/txt/privacy_policy.txt')
    ]
    context = {'content': lines}
    return render(request, 'home/privacy_policy.html', context)


def terms_and_conditions(request):
    """
    Terms & conditions page
    """
    lines = [
        line.strip()
        for line in open('home/static/home/txt/terms-and-conditions.txt')
    ]
    context = {'content': lines}
    return render(request, 'home/terms_and_conditions.html', context)
