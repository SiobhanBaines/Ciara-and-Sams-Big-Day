from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    """ View to return the index page """
    return render(request, 'home/index.html')


def register_request(request):
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
