from django.shortcuts import render_to_response,HttpResponse
from django.views.generic import DetailView
from traindb.models import Trip, Train,Station

# Create your views here.


def hello(request):
    return render_to_response('test.html')


class TripDetail(DetailView):
    model = Trip
    context_object_name = 'tripping_list'
    template_name = 'traindb/trip_list.html'
    '''
    def get_context_data(self, **kwargs):
        context = super(TripDetail, self).get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        return context

    '''
