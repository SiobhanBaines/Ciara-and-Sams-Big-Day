from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = (
            'course',
            'menu_item',
            'description'
        )
    ordering = ('course', 'menu_item')


admin.site.register(Menu, MenuAdmin)
