from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler

def say_hello(request):
    return HttpResponse(123)