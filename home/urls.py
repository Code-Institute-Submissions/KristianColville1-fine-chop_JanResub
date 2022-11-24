from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('about/', views.get_about_page, name='about'),
]
