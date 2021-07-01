from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
from .forms import NewUserForm, RSVPForm
from django.contrib.auth import login
from django.contrib import messages
from guests.models import Guest
from django.contrib.auth.models import User, Group
# from django.contrib.auth.decorators import login_required


def index(request):
    """ View to return the index page """
    return render(request, 'home/index.html')


def register_request(request):
    """ Set new user to staff on registration """
    # Code originally created by Jaysha of Ordinary Coders with the addition of the 'is_staff' object.
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect("home")

        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm
    template = 'home/register.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def rsvp(request):
    """ View to return the RSVP page,
    add group accepted or declined to User
    and set flag on Guest  """

    if request.method == 'POST':
        # convert form to dict
        form = dict(request.POST)
        # loop through form to get details of each guest in the invitation group
        for num in range(len(form['id'])):

            guest_id = form['id'][num]
            guest = get_object_or_404(Guest, id=guest_id)
            guest.group_id = form['group_id'][num]
            guest.accepted = form['rsvp_response'][num]
            guest.save()
            # If a guest accepts, this needs to be saved for adding the user group later
            if guest.accepted == 'Accept':
                response = 'accepted'
            elif guest.accepted == 'Decline':
                response = 'declined'
            else:
                response = None
        # Pick up the appropriate user group (accepted / declined)
        if response is not None:
            group = Group.objects.get(name=response)
            # Pick up the user details
            user = get_object_or_404(User, username=guest.group_id)
            # Add the group to the user
            user.groups.add(group)
        return redirect("home")

    form = RSVPForm
    guests = Guest.objects.filter(group_id=request.user)
    template = 'home/rsvp.html'
    context = {
        'guests': guests,
        'form': form,
    }

    return render(request, template, context)
