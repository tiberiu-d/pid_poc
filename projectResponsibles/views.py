from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ProjectResponsible

def responsible_list(request):
    responsible_list = ProjectResponsible.objects.all()
    context = {
        "project_responsibles": responsible_list,
    }
    return render(request, "projectResponsibles/responsibles_list.html", context)

def responsible_detail(request, pk):
    responsible = ProjectResponsible.objects.get(id=pk)
    context = {
        'responsible': responsible,
    }
    return render(request, "projectResponsibles/responsible.html", context)
