from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .models import Checkout
from guests.models import Guest
from .forms import CheckoutForm, GuestForm

import stripe


@require_POST
def cache_checkout_data(request):
    # request.session['']
    # Taken from CI Stripe Part 14 and modified for site data
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'amount': request.POST.get('checkout_form.gift_amount'),
            # 'amount': json.dumps(request.session.get('gift_amount', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        # print('line 28', gift_amount, amount, save_info, username)
        return HttpResponse(status=200)
    except Exception as e:
        print(e)
        messages.error(request, 'Sorry, you payment cannot be \
            processed at the moment. Please try later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Get the gift amount from the template
        checkout_data = {
            'gift_amount': request.POST['gift_amount'],
        }
        # Get the billing details from the template
        guest_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['gift_amount'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'email': request.POST['email'],
        }
        checkout_form = CheckoutForm(checkout_data)
        guest_form = GuestForm(guest_data)
        if checkout_form.is_valid() and guest_form.is_valid():
            # Create Checkout record
            guest = get_object_or_404(Guest, group_id=request.user)
            checkout = checkout_form.save(commit=False)
            checkout.group_id = guest
            checkout.save()

            # Update Guest record
            # guest_query = Guest.objects.filter(group_id=request.user)
            form = dict(request.POST)
            for num in range(len(form['group_id'])):
                if (form['first_name'][num] == guest.first_name) and (
                        form['last_name'][num] == guest.last_name):
                    guest.email = form['email'][num]
                    email = guest.email
                    guest.gift_chosen = True
                    guest.gift_name = 'Money'
                    guest.gift_value = guest.gift_value + checkout.gift_amount
                    guest.save()

            stripe_total = round(checkout.gift_amount * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            request.session['save_info'] = 'save-info' in request.POST

            email = 'siobhan.baines@gmail.com'
            if not email:
                messages.error(request, ('There was an error with your form. '
                                         'Please double check your information.'))
            else:
                return redirect(reverse(
                    'checkout_success',
                    args=[checkout.donation_number, email]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        gift_amount = int(request.session['gift_amount'])
        stripe_total = round(gift_amount * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        checkout_form = CheckoutForm()
        guest_form = GuestForm()

    if not stripe_public_key:
        messages.warning(
            request, 'Stripe public key is missing from your environment.')

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


def checkout_success(request, donation_number, email):
    """
    Handle successful checkouts
    """
    # Taken from CI Stripe and modified to fit site requirements
    messages.success(request, f'Gift successfully processed! \
        Your gift donation number is {donation_number}. A confirmation \
        email will be sent to {email}.')

    form = CheckoutForm
    checkout = get_object_or_404(Checkout, donation_number=donation_number)
    template = 'checkout/checkout_success.html'
    context = {
        'email': email,
        'checkout': checkout,
        'form': form,

    }

    return render(request, template, context)
