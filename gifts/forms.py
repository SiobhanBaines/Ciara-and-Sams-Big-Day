from django import forms
from .models import Gift
from .widgets import CustomClearableFileInput


class GiftForm(forms.ModelForm):

    class Meta:
        model = Gift
        fields = [
            'name',
            'description',
            'supplier_url',
            'price',
            'image_url',
            'image',
            'selected',
            'group_id',
        ]

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
