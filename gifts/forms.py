from django import forms
from .models import Gift


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
        )
