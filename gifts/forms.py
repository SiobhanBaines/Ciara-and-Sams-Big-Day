from django import forms
from .models import Gift
# from guests.models import Guest
from .widgets import CustomClearableFileInput


class GiftForm(forms.ModelForm):

    class Meta:
        model = Gift
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
    #     'name',
    #     'description',
    #     'selected',
    #     'supplier_url',
    #     'price',
    #     'image_url',
    #     'image',
    #     'group_id',
    # )
