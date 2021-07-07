from django.contrib import admin
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'event',
    )
    ordering = ('time',)


admin.site.register(Schedule)
