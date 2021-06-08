from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def type_list(request):
    return HttpResponse("This is a TYPE page")
