from django.contrib import admin
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'event',
        )


admin.site.register(Schedule, ScheduleAdmin)
