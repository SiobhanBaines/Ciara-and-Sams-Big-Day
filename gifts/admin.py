from django.contrib import admin
from .models import Gift


class GiftAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'description',
            'selected',
            'supplier_url',
            'price',
            'image_url',
            'image',
        )
    ordering = ('name', )


admin.site.register(Gift, GiftAdmin)
