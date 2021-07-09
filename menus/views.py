from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Menu
from guests.models import Guest
from .forms import MenuForm, GuestForm

import io
import csv


@login_required
def menus(request):
    """ View a list of all menus """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menus = Menu.objects.all()

    if request.method == "POST":
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['menu_csv'].file)
        print('paramFile ', paramFile)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        print(portfolio1)
        list_of_dict = list(portfolio1)

        objs = []
        for row in list_of_dict:
            objs.append(
                Menu(
                    course=row['course'],
                    menu_item=row['menu_item'],
                    description=row['description'],
                )
            )
        try:
            print('try success')
            msg = Menu.objects.bulk_create(objs)
            messages.success(request, 'Imported successfully')
        except Exception as e:
            print('error importing')
            messages.error(request, 'Error While Importing Data: ', e)
            return HttpResponse(content=e, status=400)

        return redirect('menus')

    form = MenuForm()
    context = {
        'menus': menus,
        'form': form,
    }

    return render(request, 'menus/menus.html', context)


@login_required
def menu_detail(request, menu_id):
    """ View of menu details """

    menus = Menu.objects.all()
    form = MenuForm()
    context = {
        'menus': menus,
        'form': form,
    }

    return render(request, 'menus/menu_detail.html', context)


@login_required
def add_menu(request):
    """ Add menu to menu list """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            # save data from form into model
            menu = form.save()

            # get newly create model details
            menu.id
            menu = form.save()

            messages.success(request, 'Successfully added a new menu')
            return redirect(reverse('menus'))
        else:
            messages.error(request, 'Failed to add menu. \
                           Please check the information is valid')
    else:
        form = MenuForm()

    form = MenuForm()

    template = 'menus/add_menu.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_menu(request, menu_id):
    """ Edit an Event """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menu = get_object_or_404(Menu, pk=menu_id)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the menu')
            return redirect(reverse('menus'))
        else:
            messages.error(request, 'Failed to update menu. \
                           Please check the information is valid')
    else:
        form = MenuForm(instance=menu)
        messages.info(
            request, 'You are editing an event')

    template = 'menus/edit_menu.html'
    context = {
        'form': form,
        'menu': menu,
    }

    return render(request, template, context)


@login_required
def delete_menu(request, menu_id):
    """ Delete a menu """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menu = get_object_or_404(Menu, pk=menu_id)
    menu.delete()
    # form = MenuForm(instance=menu)
    messages.success(
        request, 'Menu event deleted')
    return redirect(reverse('menus'))


@login_required
def menu_selection(request):
    """ View of menu details """
    if request.method == 'POST':
        form = dict(request.POST)
        print('line 162 form', form)
        # loop through form to get details of
        # each guest in the invitation group
        # for num in range(len(form['menu_item'])):
        for num in range(len(form['id'])):
            print('num', num)
            guest_id = form['id'][num]
            guest = get_object_or_404(Guest, id=guest_id)
            print('guest_id', guest_id)
            guest.start = form['starter'][num]
            guest.main = form['main'][num]
            guest.dessert = form['dessert'][num]
            print(guest.dessert)
            special = form['special'][num]
            print(special)
            if guest.starter and guest.main and guest.dessert:
                guest.meal_chosen = True
            else:
                if special:
                    guest.special_diet = True
                    messages.info(request, 'Please fill in the box below with \
                        details of you special requirements. Thank you.')
                else:
                    messages.error(request, 'You have not chosen enough courses. \
                        Please select a dish for each course')
            
            # guest_id = form[]
            guest.save()
            # If a guest accepts, this needs to be saved
            # for adding the user group later

        return redirect("menus")
           
    guests = Guest.objects.filter(group_id=request.user)
    menus = Menu.objects.all()
    s = 0
    m = 0
    d = 0
    for menu in menus:
        print('menu.course ', menu.course)
        print('menu_item ', menu.menu_item)
        if menu.course == "starter":
            s += 1
            if s == 1:
                starter_1 = str(menu.menu_item)
            elif s == 2:
                starter_2 = str(menu.menu_item)
            else:
                messages.error(request, 'Too many starters. Only 2 allowed')
        elif menu.course == 'main':
            m += 1
            if m == 1:
                main_1 = str(menu.menu_item)
            elif m == 2:
                main_2 = str(menu.menu_item)
            else:
                messages.error(request, 'Too many main coures. Only 2 allowed')
        elif menu.course == 'dessert':
            d += 1
            if d == 1:
                dessert_1 = str(menu.menu_item)
            elif d == 2:
                dessert_2 = str(menu.menu_item)
            else:
                messages.error(request, 'Too many desserts. Only 2 allowed')

    context = {
        'menus': menus,
        'guests': guests,
        'guest_form': GuestForm(),
        'starter_1': starter_1,
        'starter_2': starter_2,
        'main_1': main_1,
        'main_2': main_2,
        'dessert_1': dessert_1,
        'dessert_2': dessert_2
    }

    return render(request, 'menus/menu_selection.html', context)