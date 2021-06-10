from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guests, name='guests'),
    path('', views.upload_guest_list, name='upload_guest_list'),
]
