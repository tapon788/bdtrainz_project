"""bdtrainz_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from traindb.views import hello,TrainStations

from traindb.views import hello

urlpatterns = [
    url(r'prip(?P<slug>[0-9]{1,3})/$', hello, {'foo': 'bar'}, name='train_detail',),
    url(r'trip/([\w-]+)/$', TrainStations.as_view(), name='trip_detail'),
]
