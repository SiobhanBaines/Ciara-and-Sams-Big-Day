from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Schedule
from .forms import ScheduleForm

import io
import csv


@login_required
def schedules(request):
    """ View a list of all schedules """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    schedules = Schedule.objects.all()

    if request.method == "POST":
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['schedule_csv'].file)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        print(portfolio1)
        list_of_dict = list(portfolio1)

        objs = []
        for row in list_of_dict:
            objs.append(
                Schedule(
                    time=row['time'],
                    event=row['event'],
                )
            )
        try:
            Schedule.objects.bulk_create(objs)
            messages.success(request, 'Imported successfully')
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            return HttpResponse(content=e, status=400)

        return redirect('schedules')

    form = ScheduleForm()
    context = {
        'schedules': schedules,
        'form': form,
    }

    return render(request, 'schedules/schedules.html', context)


@login_required
def display_schedule(request):
    """ View of schedule details """

    schedules = Schedule.objects.all()
    form = ScheduleForm()
    context = {
        'schedules': schedules,
        'form': form,
    }

    return render(request, 'schedules/display_schedule.html', context)


@login_required
def add_schedule(request):
    """ Add schedule to schedule list """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            # save data from form into model
            schedule = form.save()

            # get newly create model details
            schedule.id
            schedule = form.save()

            messages.success(request, 'Successfully added a new schedule')
            return redirect(reverse('schedules'))
        else:
            messages.error(request, 'Failed to add schedule. \
                           Please check the information is valid')
    else:
        form = ScheduleForm()

    form = ScheduleForm()

    template = 'schedules/add_schedule.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_schedule(request, schedule_id):
    """ Edit an Event """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    schedule = get_object_or_404(Schedule, pk=schedule_id)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the schedule')
            return redirect(reverse('schedules'))
        else:
            messages.error(request, 'Failed to update schedule. \
                           Please check the information is valid')
    else:
        form = ScheduleForm(instance=schedule)
        messages.info(
            request, 'You are editing an event')

    template = 'schedules/edit_schedule.html'
    context = {
        'form': form,
        'schedule': schedule,
    }

    return render(request, template, context)


@login_required
def delete_schedule(request, schedule_id):
    """ Delete a schedule """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule.delete()
    # form = ScheduleForm(instance=schedule)
    messages.success(
        request, 'Schedule event deleted')
    return redirect(reverse('schedules'))
