from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menu, name='menu'),
    path('<int:menu_item_id>/',
         views.get_menu_item_detail,
         name='item_details'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('edit/<int:menu_item_id>/', views.edit_menu_item,
         name='edit_menu_item'),
    path('delete/<int:menu_item_id>/',
         views.delete_menu_item,
         name='delete_menu_item'),
]
