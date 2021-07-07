from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedules, name='schedules'),
    path('', views.display_schedule, name='display_schedule'),
    path('add/', views.add_schedule, name='add_schedule'),
    path('edit/<int:schedule_id>/', views.edit_schedule, name='edit_schedule'),
    path(
        'delete/<int:schedule_id>/',
        views.delete_schedule, name='delete_schedule'),
]
