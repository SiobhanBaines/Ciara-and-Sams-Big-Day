from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):

    readonly_fields = ('donation_number', 'date',)

    fields = ('donation_number', 'group_id', 'date', 'gift_amount',)

    list_display = ('donation_number', 'group_id', 'date', 'gift_amount',)

    ordering = ('date',)

admin.site.register(Donation, DonationAdmin)