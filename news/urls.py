from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path("new", views.news, name="new"),
]
