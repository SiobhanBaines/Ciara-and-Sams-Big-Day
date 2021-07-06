from django.db import models


class Schedule(models.Model):    
    time = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.time
