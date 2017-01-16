from django.shortcuts import get_object_or_404
from django.views.generic import DetailView,ListView
from traindb.models import Trip, Train, Station

# Create your views here.


class TrainStations(ListView):
    model = Station



    def get_queryset(self):

        self.station = get_object_or_404(Station, name = self.args[0])

        # self.trip = get_object_or_404(Trip, start_station=self.station)
        # self.train= get_object_or_404(Train,trip = self.trip)

        return Trip.objects.filter(start_station=self.station)

    def get_context_data(self, **kwargs):
        context = super(TrainStations, self).get_context_data(**kwargs)

        context['station_list'] = Train.objects.all()
        return context