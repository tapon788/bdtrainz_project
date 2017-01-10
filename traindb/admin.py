from django.contrib import admin

from traindb.models import Train, Station, Trip
# Register your models here.


class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'offday')

admin.site.register(Station)
admin.site.register(Trip)
admin.site.register(Train)
