from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .models import Checkout, Guest
from .forms import CheckoutForm, GuestForm

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    guest = get_object_or_404(Guest, group_id=request.user)
    print('line 15, guest', guest)

    # checkout_form = CheckoutForm(request.POST, request.FILES)

    stripe_total = round(51.25 * 100)   # add checkout.gift_amount
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print('line 23, intent', intent)

    checkout_form = CheckoutForm()
    guest_form = GuestForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing from your environment.')

    template = 'checkout/checkout.html'
    context = {
        'guest': guest,
        'guest_form': guest_form,
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
