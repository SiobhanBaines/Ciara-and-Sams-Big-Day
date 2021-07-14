from django.test import TestCase
from .forms import MenuForm


class TestCheckoutForm(TestCase):

    # def test_first_name_required(self):
    #     form = GuestForm({'first_name': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('first_name', form.errors.keys())
    #     self.assertEqual(
    #         form.errors['first_name'][0], 'This field is required.')

    # def test_last_name_required(self):
    #     form = GuestForm({'last_name': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('last_name', form.errors.keys())
    #     self.assertEqual(
    #         form.errors['last_name'][0], 'This field is required.')

    # def test_postcode_required(self):
    #     form = GuestForm({'postcode': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('postcode', form.errors.keys())
    #     self.assertEqual(form.errors['postcode'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MenuForm()
        self.assertEqual(form.Meta.fields, ['course', 'menu_item'])
