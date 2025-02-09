from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Asset(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField(max_length=150)

     def __str__(self):
          return self.name
     
     def get_absolute_url(self):
        return reverse('asset-detail', kwargs={'pk': self.id})

class Event(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    people = models.IntegerField()
    assets = models.ManyToManyField(Asset)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'event_id': self.id})
    
class Moment(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField('Date & Time')

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
            return f'{self.name} on {self.date_time}'
    
    class Meta:
         ordering = ['date_time']

