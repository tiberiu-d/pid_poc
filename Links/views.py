from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def links_view(request):
    return HttpResponse("Looking at the LINKS page")
