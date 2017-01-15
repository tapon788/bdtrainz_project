from django.shortcuts import render_to_response,HttpResponse
from django.views.generic import DetailView
from traindb.models import Trip, Train, Station

# Create your views here.
def hello(request):
    return render_to_response('test.html')


class StationDetail(DetailView):
    model = Station
    context_object_name = 'tripping_list'
    slug_field = 'train_list'

    def get_context_data(self, **kwargs):
        context = super(StationDetail, self).get_context_data(**kwargs)
        context['train_list'] = Train.objects.all()
        return context
