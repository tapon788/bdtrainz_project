from django.shortcuts import render_to_response,HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView,ListView
from traindb.models import Trip, Train, Station

# Create your views here.
def hello(request, slug, foo):

    return HttpResponse("Hellow World "+slug+' '+foo)


class TrainStations(ListView):
    template_name = 'traindb/trip_list.html'
    context_object_name = 'tripping_list'

    def get_queryset(self):
        self.station = get_object_or_404(Station, name = self.args[0])
        self.trip = get_object_or_404(Trip, start_station=self.station)
        self.train= get_object_or_404(Train,trip = self.trip)
        return Train.objects.filter(trip=self.trip)