from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Gift
from django.contrib.auth.models import User
from .forms import GiftForm

import io
import csv

@login_required
def gifts(request):
    """ View a list of all Gifts """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    gifts = Gift.objects.all()
    # query = None

    # if request.GET:
        # if 'q' in request.GET:
        #     query = request.GET['q']
        #     if not query:
        #         messages.error(
        #             request, "You didn't enter any search criteria.")
        #         return redirect(reverse('Gifts'))

    if request.method == "POST":
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['gift_list_csv'].file)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)

        objs = []
        for row in list_of_dict:
            objs.append(
                Gift(
                    name=row['name'],
                    description=row['description'],
                    selected=False,
                    supplier_url=row['supplier_url'],
                    price=row['price'],
                    image_url=row['image_url'],
                    image=row['image'],
                )
            )
        try:
            msg = Gift.objects.bulk_create(objs)
            # returnmsg = {"status_code": 200}
            messages.error(request, 'Imported successfully')
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            return HttpResponse(content=e, status=400)

        return redirect('gifts')

    context = {
        'gifts': gifts,
    }

    return render(request, 'gifts/gifts.html', context)


@login_required
def view_gift(request, gift_id):
    """ View individual Gift details """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    gift = get_object_or_404(Gift, pk=gift_id)
    context = {
        'gift': gift,
    }

    return render(request, 'gifts/view_gift.html', context)


@login_required
def add_gift(request):
    """ Add Gift to Gift list """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES)
        if form.is_valid():
            # save data from form into model
            gift = form.save()

            # get newly create model details
            gift.id

            gift = form.save()

            messages.success(request, 'Successfully added a new Gift')
            return redirect(reverse('view_gift', args=[gift.id]))
        else:
            messages.error(request, 'Failed to add gift. Please check the information is valid')
    else:
        form = GiftForm()

    form = GiftForm()

    template = 'gifts/add_gift.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_gift(request, gift_id):
    """ Edit a Gift """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    gift = get_object_or_404(Gift, pk=gift_id)

    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES, instance=gift)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the Gift')
            return redirect(reverse('view_gift', args=[gift.id]))
        else:
            messages.error(request, 'Failed to add Gift. Please check the information is valid')
    else:
        form = GiftForm(instance=gift)
        messages.info(
            request, f'You are editing {gift.name}')
    template = 'gifts/edit_gift.html'
    context = {
        'form': form,
        'gift': gift,
    }

    return render(request, template, context)


@login_required
def delete_gift(request, gift_id):
    """ Delete a Gift """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    gift = get_object_or_404(Gift, pk=gift_id)
    Gift.delete()
    messages.success(request, 'Gift deleted')
    return redirect(reverse('gifts'))
