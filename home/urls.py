from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('about/', views.get_about_page, name='about'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_and_condition/',
         views.terms_and_conditions,
         name='terms_and_conditions')
]
