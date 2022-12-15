from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .main_functions import mh_fill_timetable
import json

# Create your views here.
# request handler

def mh_fill_timetable(request): 
    input = json.loads(request.body) 
    output = mh_fill_timetable(input)
    return JsonResponse(output)