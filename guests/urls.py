from django.urls import path
# from django.contrib.auth import views
# from .views import UploadGuestListView
from . import views

urlpatterns = [
    path('', views.all_guests, name='guests'),
    path('<int:guest_id>/', views.view_guest, name='view_guest'),
    path('add/', views.add_guest, name='add_guest'),
]
