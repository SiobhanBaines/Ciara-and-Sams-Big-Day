from django.urls import path
from . import views

urlpatterns = [
    path('', views.gifts, name='gifts'),
    path('<int:gift_id>/', views.gift_detail, name='gift_detail'),
    path('add/', views.add_gift, name='add_gift'),
    path('edit/<int:gift_id>/', views.edit_gift, name='edit_gift'),
    path('delete/<int:gift_id>/', views.delete_gift, name='delete_gift'),
    path('gift_donation/<int:gift_amount>/',
         views.gift_donation, name='gift_donation'),
]
