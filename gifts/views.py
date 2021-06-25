from django.shortcuts import render, reverse, redirect, get_object_or_404
# from django.views import View
from django.http import HttpResponse
# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Gift
# from django.contrib.auth.models import User, Group
from .forms import GiftForm

import io
import csv


@login_required
def gifts(request):
    """ View a list of all Gifts """
    # print('request.user.is_staff', request.user.is_staff)
    # print('request.user.is_superuser', request.user.is_superuser)
    # print('request.user.group.has_group', request.user | has_group)
    # if not request.user.is_superuser or not request.user.is_staff or not request.user | has_group:
    #     messages.error(request, 'Sorry, only the bride and groom can do that.')
    #     return redirect(reverse('home'))

    gifts = Gift.objects.all()

    if request.method == "POST":
        if request.user.is_staff or request.user.is_superuser:
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
def gift_detail(request, gift_id):
    """ View individual Gift details """
    # if not request.user.is_superuser or not request.user.is_staff:
    #     messages.error(request, 'Sorry, only the bride and groom can do that.')
    #     return redirect(reverse('home'))
    print('gift_id', gift_id)
    gift = get_object_or_404(Gift, pk=gift_id)
    print(gift)
    context = {
        'gift': gift,
    }
    print('line 77')
    return render(request, 'gifts/gift_detail.html', context)


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
            print('line 100')
            return redirect(reverse('gift_detail', args=[gift.id]))
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
            print('line 131')
            return redirect(reverse('gift_detail', args=[gift.id]))
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
