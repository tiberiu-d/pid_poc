from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, ProjectType
# Create your views here.


def project_list(request):
    all_projects = Project.objects.all()
    all_projects_count = Project.objects.count()

    context = {
        'projects': all_projects,
        'count': all_projects_count,
    }
    return render(request, "Projects/projects_view.html", context)


def project_create(request):
    return HttpResponse("This is the PROJECT CREATE page")


def project_read(request, pk):
    return HttpResponse("This is the PROJECT DETAILED VIEW page")


def project_update(request, pk):
    return HttpResponse("This is the PROJECT UPDATE page")


def project_delete(request, pk):
    return HttpResponse("This is the PROJECT DELETE page")
