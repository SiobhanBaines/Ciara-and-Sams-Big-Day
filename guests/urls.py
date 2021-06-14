from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guests, name='guests'),
    path('<int:guest_id>/', views.view_guest, name='view_guest'),
    path('add/', views.add_guest, name='add_guest'),
    path('edit/<int:guest_id>/', views.edit_guest, name='edit_guest'),
]
