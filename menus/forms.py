from django import forms
from .models import Menu
from guests.models import Guest


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ['course', 'menu_item', ]
        # fields = '__all__'


class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = (
            'group_id',
            'first_name',
            'starter',
            'main',
            'dessert',
            'special_diet',
            'requirements',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'group_id': 'group_id',
            'first_name': 'first_name',
            'starter': 'starter',
            'main': 'main',
            'dessert': 'dessert',
            'special_diet': 'special_diet',
            'requirements': 'requirements',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
