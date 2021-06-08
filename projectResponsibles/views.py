from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def responsible_list(request):
    return HttpResponse("This is a USER page")
