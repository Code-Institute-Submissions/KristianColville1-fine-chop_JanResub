from django.shortcuts import render


def get_menu(request):
    return render(request, 'menu/index.html')
