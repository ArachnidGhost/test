from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    user_email = models.EmailField(null=False)
    user_name = models.CharField(max_length=255, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    available_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user_email} - {self.event.name if self.event else 'no event'}"