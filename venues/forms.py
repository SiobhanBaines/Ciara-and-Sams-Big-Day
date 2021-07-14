from django import forms
from .models import Venue
from .widgets import CustomClearableFileInput


class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
