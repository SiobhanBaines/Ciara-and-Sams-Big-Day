from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = (
            'course',
            'name',
            'description'
        )
    ordering = ('course', 'name')


admin.site.register(Menu, MenuAdmin)
