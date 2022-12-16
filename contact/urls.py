from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('careers/', views.careers, name='careers'),
]
