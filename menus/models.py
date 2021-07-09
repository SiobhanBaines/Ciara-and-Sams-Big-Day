from django.db import models


class Menu(models.Model):
    course = models.CharField(max_length=20, null=False, blank=False)
    menu_item = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
