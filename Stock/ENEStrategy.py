from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import json

def ENE(request):
    return render_to_response('ENE.html')
#     return HttpResponse("Hello world ! ")

