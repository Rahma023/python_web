from django.db import models

# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=200)
    event_date_and_time=models.DateField()
    event_id=models.CharField(max_length=12)
    event_duration=models.DurationField()
    event_signed_by=models.CharField(max_length=200)
    event_approved_by=models.CharField(max_length=200)
    event_participants=models.CharField(max_length=250)

