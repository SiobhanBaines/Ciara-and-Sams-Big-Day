# created by  fuser60596 in Stackoverflow 6 may 2017
from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    user.groups.add(group)

    return True if group in user.groups.all() else False
