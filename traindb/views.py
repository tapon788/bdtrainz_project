from django.shortcuts import render_to_response,HttpResponse
from django.views.generic import DetailView
from traindb.models import Trip, Train

# Create your views here.
def hello(request):
    return render_to_response('test.html')


class TrainDetail(DetailView):
    model = Train
    context_object_name = 'tripping_list'

    def get_context_data(self, **kwargs):
        context = super(TrainDetail, self).get_context_data(**kwargs)
        context['trip_list'] = Trip.objects.all()
        return context
