from django import forms
from .models import Menu
from guests.models import Guest


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = '__all__'


class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = 'first_name',
