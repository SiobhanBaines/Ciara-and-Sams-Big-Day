from django.db import models


class Schedule(models.Model):
    time = models.CharField(max_length=5, null=False, blank=False)
    event = models.CharField(max_length=254, null=False, blank=False)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return self.time
