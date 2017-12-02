from django.shortcuts import render
from pindropapp.models import Pin
import json
from django.core import serializers

# Create your views here.


from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def pins(request):
    allpins = list(Pin.objects.all())
    return HttpResponse(serializers.serialize("json",allpins), content_type = "application/json")

@csrf_exempt
def addpin(request):
    pin_data=json.loads(request.body)
    newpin = Pin(
        type=pin_data["type"], 
        latitude=pin_data["latitude"], 
        longitude=pin_data["longitude"], 
        cross_street=pin_data["cross_street"], 
        rating=pin_data["rating"])

    newpin.save()
    return HttpResponse(serializers.serialize("json",[newpin]), content_type = "application/json")



