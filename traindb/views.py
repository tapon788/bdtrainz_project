from django.shortcuts import render_to_response,HttpResponse


# Create your views here.
def hello(request):
    return render_to_response('test.html')

