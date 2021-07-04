from django import forms
from .models import Gift
from guests.models import Guest


class GiftForm(forms.ModelForm):

    class Meta:
        model = Gift
        fields = (
            'name',
            'description',
            'selected',
            'supplier_url',
            'price',
            'image_url',
            'image',
            'group_id',
        )
