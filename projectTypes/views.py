from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import ProjectType
from .forms import TypeModelForm
# Create your views here.

def types_list(request):
    types = ProjectType.objects.all()
    count = ProjectType.objects.count()
    context = {
        'types': types,
        'count': count,
    }
    return render(request, 'projectTypes/types_list.html', context)

def types_create(request):
    form = TypeModelForm()
    if request.method == "POST":
        form = TypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projects/types/')
    context = {
        'form': form
    }

    return render(request, 'projectTypes/types_create.html', context)

def types_read(request, pk):
    return HttpResponse("Work in progress")

def types_update(request, pk):
    type = ProjectType.objects.get(id=pk)
    form = TypeModelForm(instance=type)

    if request.method == "POST":
        form = TypeModelForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('/projects/types/')
    context = {
        "form": form,
        "type": type,
    }
    return render(request, "projectTypes/types_update.html", context)

def types_delete(request, pk):
    type = ProjectType.objects.get(id=pk)
    type.delete()
    return redirect('/projects/types/')
