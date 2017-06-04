from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import json

def Volume(request):
    return render_to_response('VolumeAndPrice.html')
#     return HttpResponse("Hello world ! ")