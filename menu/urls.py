from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menu, name='menu'),
    path('<str:str>/', views.get_food_menu, name='food_menu'),
]
