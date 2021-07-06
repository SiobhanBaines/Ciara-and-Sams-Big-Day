from django.urls import path
from . import views

urlpatterns = [
    path('', views.venues, name='venues'),
    path('add/', views.add_venue, name='add_venue'),
    path('edit/<int:venue_id>/', views.edit_venue, name='edit_venue'),
    path('delete/<int:venue_id>/', views.delete_venue, name='delete_venue'),
]
