from django.shortcuts import render, reverse, redirect, get_object_or_404
# from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Venue
from .forms import VenueForm

import os


@login_required
def venues(request):
    google_maps_key = settings.GOOGLE_MAPS_KEY
    """ View a list of all venues """
    venues = Venue.objects.all()

    form = VenueForm()

    template = 'venues/venues.html'
    context = {
        'venues': venues,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_venue(request):
    """ Add venue to venue list """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            # save data from form into model
            venue = form.save()

            # get newly create model details
            venue.id

            venue = form.save()

            messages.success(request, 'Successfully added a new venue')
            return redirect(reverse('venues'))
        else:
            messages.error(
                request, 'Failed to add venue. \
                    Please check the information is valid')
    else:
        form = VenueForm()

    form = VenueForm()

    template = 'venues/add_venue.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_venue(request, venue_id):
    """ Edit a venue """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    venue = get_object_or_404(Venue, pk=venue_id)

    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES, instance=venue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the venue')
            return redirect(reverse('venues'))
        else:
            messages.error(
                request, 'Failed to add venue. \
                    Please check the information is valid')
    else:
        form = VenueForm(instance=venue)
        messages.info(
            request, f'You are editing {venue.name}')

    template = 'venues/edit_venue.html'
    context = {
        'form': form,
        'venue': venue,
    }

    return render(request, template, context)


@login_required
def delete_venue(request, venue_id):
    """ Delete a venue """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    venue = get_object_or_404(Venue, pk=venue_id)

    image_file = 'media/' + str(venue.image)
    if os.path.exists(image_file):
        os.remove(image_file)

    venue.delete()
    messages.success(request, f'venue {venue.name} deleted')
    return redirect(reverse('venues'))
