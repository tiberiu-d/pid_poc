from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import ProjectResponsible
from .forms import ResponsibleForm

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


def responsible_create(request):
    form = ResponsibleForm()

    if request.method == 'POST':
        form = ResponsibleForm(request.POST)

        if form.is_valid():
            new_name = form.cleaned_data["full_name"]
            new_email = form.cleaned_data["email"]

            ProjectResponsible.objects.create(
                full_name=new_name,
                email=new_email,
            )
            return redirect('/projects/responsibles/')

    context = {
        "form": form,
    }
    return render(request, "projectResponsibles/responsible_create.html", context)
