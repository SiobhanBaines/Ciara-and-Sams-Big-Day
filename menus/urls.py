from django.urls import path
from . import views

urlpatterns = [
    path('', views.menus, name='menus'),
    path('display_menu/', views.display_menu, name='display_menu'),
    path('add/', views.add_menu, name='add_menu'),
    path('edit/<int:menu_id>/', views.edit_menu, name='edit_menu'),
    path('delete/<int:menu_id>/', views.delete_menu, name='delete_menu'),
    path('menu_selection/', views.menu_selection, name='menu_selection'),
]
