from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register_request, name='register_request'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('contact/', views.contact, name='contact'),
    # path('success/', views.success, name='success'),
]
