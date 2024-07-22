from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    people = models.IntegerField()

    def __str__(self):
        return self.name