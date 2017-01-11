from django.contrib import admin
from traindb.models import Train, Station, Trip
# Register your models here.


class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'offday', 'trip')
    search_fields = ('name', 'trip__start_station__name')


class TripAdmin(admin.ModelAdmin):
    list_display = ('start_station', 'start_time', 'arrival_station', 'arrival_time')
    search_fields = ('start_station__name',)

admin.site.register(Station)
admin.site.register(Trip, TripAdmin)
admin.site.register(Train, TrainAdmin)