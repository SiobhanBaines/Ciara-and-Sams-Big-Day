from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Checkout, Guest
from .forms import CheckoutForm, GuestForm


def checkout(request):

    guest = get_object_or_404(Guest, group_id=request.user)
    print('guest', guest)
    checkout_form = CheckoutForm()
    guest_form = GuestForm()
    template = 'checkout/checkout.html'
    context = {
        'guest': guest,
        'guest_form': guest_form,
        'checkout_form': checkout_form,
        'stripe_public_key': 'pk_test_51It6A8HXaEBIcMEEvxdqfecnZpIkIA4Zkgkv4KUQtfCPH3dUwUC87f8NYvWaVnQEOJc4g1riYkLVDCoA5kDcggXv00VIN5ffWh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
