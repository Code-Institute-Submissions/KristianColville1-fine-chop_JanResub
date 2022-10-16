from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User


def get_home(request):
    return render(request, 'home/index.html')
