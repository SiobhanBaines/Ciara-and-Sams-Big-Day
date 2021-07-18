from django.db import models


class Menu(models.Model):
    course = models.CharField(max_length=20, null=False, blank=False)
    menu_item = models.CharField(max_length=250, null=False, blank=False)

    class Meta:
        ordering = ['-course']
    
    def __str__(self):
        return self.course
