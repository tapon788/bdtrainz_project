import os
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'bdtrainz_project.settings'
application = get_wsgi_application()
from traindb.models import Train, Trip, Station
from django.conf import settings
filename = os.path.join(settings.BASE_DIR+'\\traindb', 'input_all_train.txt')



fp = open(filename, 'r')
counter = 1
all_data = []
data = []
i_no = 0
i_name = 1
i_offday = 2
i_start_station = 3
i_start_time = 4
i_arrival_station = 5
i_arrival_time = 6
input_station = []
all_input_station = []
input_trip = []
all_input_trip = []

print "Deleting everything from db"
Station.objects.all().delete()
Trip.objects.all().delete()

def load_station_data(in_data):


    print in_data
    if in_data[i_start_station] not in input_station:
        station = Station()
        print in_data[i_start_station]
        input_station.append(in_data[i_start_station])
        station.name = in_data[i_start_station]
        station.save()

    if in_data[i_arrival_station] not in input_station:
        station = Station()
        input_station.append(in_data[i_arrival_station])
        station.name = in_data[i_arrival_station]
        station.save()


def load_trip_data(in_data):

    trip = Trip()

    all_input_trip.append(input_trip)
    '''
    start_station_object = Station.objects.get(name=in_data[i_start_station])
    arriv_station_object = Station.objects.get(name=in_data[i_arrival_station])
    trip.start_station = start_station_object
    trip.start_time = in_data[i_start_time]
    trip.arrival_station = arriv_station_object
    trip.arrival_time = in_data[i_arrival_time]
    trip.save()
    '''
    try:
        start_station_object = Station.objects.get(name=in_data[i_start_station])
    except Station.DoesNotExist:
        print "Start station "+in_data[i_start_station]+' Does not exist'
        return 0

    try:
        arriv_station_object = Station.objects.get(name=in_data[i_arrival_station])
    except Station.DoesNotExist:
        print "Aival st: "+in_data[i_arrival_station]+" Doest not exist"
        return 0

    input_trip.append(start_station_object)
    input_trip.append(in_data[i_start_time])
    input_trip.append(arriv_station_object)
    input_trip.append(in_data[i_arrival_time])

    if input_trip not in all_input_trip:
        all_input_trip.append(input_trip)
        trip.start_station = start_station_object
        trip.start_time = in_data[i_start_time]
        trip.arrival_station = arriv_station_object
        trip.arrival_time = in_data[i_arrival_time]
        trip.save()


for line in fp.readlines():

    data.append(line.strip())
    if counter % 8 == 0:

        data = data[1:]
        all_data.append(data)
        load_station_data(data)
        data = []

    counter += 1
counter = 1
data = []
fp.close()
fp = open(filename, 'r')
for line in fp.readlines():
    data.append(line.strip())
    if counter % 8 == 0:
        data = data[1:]
        all_data.append(data)
        load_trip_data(data)
        data = []

    counter += 1

fp.close()

print input_station
