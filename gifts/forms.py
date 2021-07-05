from django import forms
from .models import Gift
from .widgets import CustomClearableFileInput


class GiftForm(forms.ModelForm):

    class Meta:
        model = Gift
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
