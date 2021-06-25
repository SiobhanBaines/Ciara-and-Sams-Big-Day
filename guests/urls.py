from django.urls import path
from . import views

urlpatterns = [
    path('', views.guests, name='guests'),
    path('<int:guest_id>/', views.guest_detail, name='guest_detail'),
    path('add/', views.add_guest, name='add_guest'),
    path('edit/<int:guest_id>/', views.edit_guest, name='edit_guest'),
    path('delete/<int:guest_id>/', views.delete_guest, name='delete_guest'),
]
