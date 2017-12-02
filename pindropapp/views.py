from django.shortcuts import render
from pindropapp.models import Pin
import json
from django.core import serializers

# Create your views here.


from django.http import HttpResponse
import datetime
import googlemaps


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def pins(request):
    allpins = list(Pin.objects.all())
    return HttpResponse(serializers.serialize("json",allpins), content_type = "application/json")

def google_services(request):
    gmaps = googlemaps.Client(key='AIzaSyD31nwKEamghwtw7mReM5MO9uJ7KyH0S0k')

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)
    html = "<html><body>Directions are %s.</body></html>" % directions_result
    return HttpResponse(html)
