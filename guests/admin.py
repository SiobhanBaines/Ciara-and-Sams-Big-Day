from django.contrib import admin
from .models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'group_id',
        'first_name',
        'last_name',
        'plus_one',
        'address_line_1',
        'address_line_2',
        'city',
        'county',
        'country',
        'postcode',
        'email',
        'phone_number',
        'accepted',
        'meal_chosen',
        'starter',
        'main',
        'dessert',
        'gift_chosen',
        'gift_name',
        'gift_value',
    )

    ordering = ('group_id', 'first_name')


admin.site.register(Guest, GuestAdmin)
