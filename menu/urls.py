from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menu, name='menu'),
    path('<str:str>/<int:menu_item_id>/',
         views.get_menu_item_detail,
         name='item_details'),
]
