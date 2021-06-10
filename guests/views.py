from django.shortcuts import render
from .models import Guest

# Create your views here.


def all_guests(request):
    """ View a list of all guests """

    guests = Guest.objects.all()

    context = {
        'guests': guests,
    }

    return render(request, 'guests/guests.html', context)
