from django.shortcuts import render
from pindropapp.models import Pin
import json
from django.core import serializers

# Create your views here.


from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def pins(request):
    allpins = list(Pin.objects.all())
    return HttpResponse(serializers.serialize("json",allpins), content_type = "application/json")

