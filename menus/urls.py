from django.urls import path
from . import views

urlpatterns = [
    path('', views.menus, name='menus'),
    # path('<int:menu_id>/', views.menu_detail, name='menu_detail'),
    path('add/', views.add_menu, name='add_menu'),
    path('edit/<int:menu_id>/', views.edit_menu, name='edit_menu'),
    path('delete/<int:menu_id>/', views.delete_menu, name='delete_menu'),
]
