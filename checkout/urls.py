from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<donation_number>/<group_id>',
         views.checkout_success, name='checkout_success'),
    #     path('add/', views.add_gift, name='add_gift'),
    #     path('edit/<int:gift_id>/', views.edit_gift, name='edit_gift'),
    #     path('delete/<int:gift_id>/', views.delete_gift, name='delete_gift'),
]
