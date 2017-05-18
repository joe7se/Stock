from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import json

def index(request):
    return render_to_response("index.html")

