from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .models import Checkout
from guests.models import Guest
from .forms import CheckoutForm, GuestForm

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    print('request.method ', request.method)
    if request.method == 'POST':
        # form = dict(request.POST)
        # print('line 17 form', form)
        checkout_form = CheckoutForm(request.POST, request.FILES)
        if checkout_form.is_valid():
            checkout = checkout_form.save()
            print('line 19 checkout_form', checkout_form)
            guest_form = GuestForm(request.POST, request.FILES)
            if guest_form.is_valid():
                guest = guest_form.save()
                print('line 19 guest_form', guest_form)
                # Save the info to the user's profile if all is well
                request.session['save_info'] = 'save-info' in request.POST
                return redirect(reverse(
                    'checkout_success', args=[checkout.donation_number]))
            else:
                messages.error(request, ('There was an error with your form. '
                                         'Please double check your information.'))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:

        stripe_total = round(0.30 * 100)   # add checkout.gift_amount
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # print('line 23, intent', intent)
        checkout_form = CheckoutForm()
        guest_form = GuestForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing from your environment.')

    guest = get_object_or_404(Guest, group_id=request.user)
    template = 'checkout/checkout.html'
    context = {
        'guest': guest,
        'guest_form': guest_form,
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, donation_number, group_id):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    print('line 70 save_info ', save_info)
    checkout = get_object_or_404(Checkout, donation_number=donation_number)
    guest = get_object_or_404(Guest, group_id=group_id)
    messages.success(request, f'Order successfully processed! \
        Your order number is {donation_number}. A confirmation \
        email will be sent to {guest.email}.')

    template = 'checkout/checkout_success.html'
    context = {
        'checkout': checkout,
    }

    return render(request, template, context)