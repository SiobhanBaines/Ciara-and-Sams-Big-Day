from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import NewUserForm, RSVPForm, ContactForm
from django.contrib.auth import login
from django.contrib import messages
from guests.models import Guest
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth.decorators import login_required


def index(request):
    """ View to return the index page """

    if not request.user.is_superuser and not request.user.is_staff:
        guests = Guest.objects.filter(group_id=request.user)
        guest_names = [guest.first_name for guest in guests]
        guest_name = ", ".join(guest_names)
        accepteds = [guest.accepted for guest in guests]
        accepted = ", ".join(accepteds)
    else:
        guest_name = ''

    template = 'home/index.html'
    context = {
        'guest_name': guest_name,
    }

    return render(request, template, context)


def register_request(request):
    """ Set new user to staff on registration """
    # staff_secret = settings.STAFF_SECRET
    # Code originally created by Jaysha of Ordinary Coders
    #   with the addition of the 'is_staff' object.

    staff_secret = settings.STAFF_SECRET

    if request.method == "POST":

        code = request.POST['code']
        form = NewUserForm(request.POST)
        if form.is_valid():
            if code == staff_secret:
                user = form.save()
                user.is_staff = True
                user.save()
                login(
                    request, user,
                    backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Registration successful.")
                return redirect("home")
            else:
                messages.error(
                    request, "The code you entered is incorrect.")

        messages.error(
            request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm
    code = ""
    template = 'home/register.html'
    context = {
        'form': form,
        'code': code,
    }

    return render(request, template, context)


@login_required
def rsvp(request):
    """ View to return the RSVP page,
    add group accepted or declined to User
    and set flag on Guest  """

    if request.method == 'POST':
        group_id = request.POST['group_id']
        # convert form to dict
        form = dict(request.POST)
        # loop through form to get details of
        #   each guest in the invitation group
        for num in range(len(form['id'])):

            guest_id = form['id'][num]
            guest = get_object_or_404(Guest, id=guest_id)
            print(guest.plus_one_first_name, guest.first_name)
            guest.group_id = form['group_id'][num]
            guest.accepted = form['rsvp_response'][num]
            guest.plus_one = form['plus_one'][num]
            print(guest.plus_one)
            if guest.plus_one == True:
                guest.plus_one_first_name = form['plus_one_first_name']
                guest.plus_one_last_name = form['plus_one_last_name']
            else:
                guest.plus_one_first_name = ' '
                guest.plus_one_last_name = ' '

            guest.message = form['message']
            guest.save()
            # If a guest accepts, this needs to be saved
            #   for adding the user group later
            if guest.accepted == 'Accept':
                response = 'accepted'
                guest.accepted = 'Accepted'
            elif guest.accepted == 'Decline':
                response = 'declined'
                guest.accepted = 'Declined'
            else:
                response = None
        # Pick up the appropriate user group (accepted / declined)
        if response is not None:
            group = Group.objects.get(name=response)
            # Pick up the user details
            user = get_object_or_404(User, username=guest.group_id)
            # Add the group to the user
            user.groups.add(group)

        rsvp_email(group_id)

        return redirect("home")

    form = RSVPForm
    guests = Guest.objects.filter(group_id=request.user)
    template = 'home/rsvp.html'
    context = {
        'guests': guests,
        'form': form,
    }

    return render(request, template, context)


@login_required
def contact(request):
    """ Contact Form """

    if request.method == 'GET':
        form = ContactForm()
    else:
        
        to_email = settings.DEFAULT_FROM_EMAIL
        send_to_email = to_email.strip("'()")
        print("line 135 ", to_email )

        form = ContactForm(request.POST)
        if form.is_valid():
            to_email = [send_to_email]
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            print("line 145 ", to_email, settings.DEFAULT_FROM_EMAIL)
            
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    to_email,
                    fail_silently=False,
                    auth_user=settings.EMAIL_HOST_USER,
                    auth_password=settings.EMAIL_HOST_PASSWORD,
                    )

            except Exception as e:
                messages.error(request, 'Something went wrong. \
                    Please try to send the email again.')
                return HttpResponse(content=e, status=400)

            messages.success(request, 'Thank you for your message.')
            return redirect('home')

    return render(request, "home/contact.html", {'form': form})


def rsvp_email(group_id):
    """ Send RSVP confirmation email """

    guests = Guest.objects.filter(group_id=group_id)

    for guest in guests:
        if guest.first_name:
            first_name = guest.first_name
        context = {
            'first_name': first_name,
        }

        # The below process for loading the email was taken from
        #   MasterCodeOnline and modifiied for the specific emails
        if guest.accepted == 'Accepted':
            subject = 'Wedding Acceptance'
            with open('home/templates/home/accept_email.txt') as f:
                rsvp_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject, body=rsvp_message,
                from_email=settings.DEFAULT_FROM_EMAIL, to=[guest.email, ])
            template = get_template('home/accept_email.html').render(context)
            message.attach_alternative(template, 'text/html')
        else:
            subject = 'Wedding Decline'
            with open('home/templates/home/decline_email.txt') as f:
                checkout_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject, body=checkout_message,
                from_email=settings.DEFAULT_FROM_EMAIL, to=[guest.email, ])
            template = get_template('home/decline_email.html').render(context)
            message.attach_alternative(template, 'text/html')

        message.send()


    def get_next_id(curr_id):
        try:
            ret = Image.objects.filter(id__gt=curr_id).order_by("id")[0:1].get().id
        except Image.DoesNotExist:
            ret = Image.objects.aggregate(Maz("id"))['id__max']
        return ret
