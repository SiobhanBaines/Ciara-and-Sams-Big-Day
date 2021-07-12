from django.db import models


class Schedule(models.Model):
    time = models.CharField(max_length=5, null=False, blank=False)
    event = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.time
