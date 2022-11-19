from django.shortcuts import render


def get_menu(request):
    return render(request, 'menu/index.html')


def get_food_menu(request, str):
    return render(request, 'menu/index.html')
