from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.index, name='index'),
    path('validate/', views.validate_email, name='validate_email'),
]
