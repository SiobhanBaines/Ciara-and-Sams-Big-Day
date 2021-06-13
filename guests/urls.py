from django.urls import path
# from django.contrib.auth import views
# from .views import UploadGuestListView
from . import views

urlpatterns = [
    path('', views.guests, name='guests'),
    # path('', views.upload_guest_list, name='upload_guest_list'),
]
