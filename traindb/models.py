from __future__ import unicode_literals

from django.db import models

# Create your models here.


# status_choices = (('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN','Sunday'))


class Station(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Trip(models.Model):
    start_time = models.TimeField()
    arrival_time = models.TimeField()
    start_station = models.ForeignKey(Station, related_name='st_station')
    arrival_station = models.ForeignKey(Station, related_name='ar_station')

    def __str__(self):
        return str(self.start_station)+' to '+str(self.arrival_station)

    def __unicode__(self):
        return str(self.start_station) + ' to ' + str(self.arrival_station)


class Train(models.Model):
    name = models.CharField(max_length=70)
    number = models.IntegerField()
    offday = models.CharField(max_length=10)
    trip = models.ForeignKey(Trip)

    def __unicode__(self):
        return self.name


