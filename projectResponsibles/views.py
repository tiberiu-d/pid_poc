from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import ProjectResponsible
from .forms import ResponsibleForm, ResponsibleModelForm

# main view
def responsible_list(request):
    responsible_list = ProjectResponsible.objects.all()
    context = {
        "project_responsibles": responsible_list,
    }
    return render(request, "projectResponsibles/responsibles_list.html", context)

# detail view
def responsible_detail(request, pk):
    responsible = ProjectResponsible.objects.get(id=pk)
    context = {
        'responsible': responsible,
    }
    return render(request, "projectResponsibles/responsible_detail.html", context)

# create view
def responsible_create(request):
    form = ResponsibleModelForm()

    if request.method == 'POST':
        form = ResponsibleModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/projects/responsibles/')
        #     new_name = form.cleaned_data["full_name"]
        #     new_email = form.cleaned_data["email"]

        #     ProjectResponsible.objects.create(
        #         full_name=new_name,
        #         email=new_email,
        #     )

    context = {
        "form": form,
    }
    return render(request, "projectResponsibles/responsible_create.html", context)

# update view
def responsible_update(request, pk):
    responsible = ProjectResponsible.objects.get(id=pk)
    form = ResponsibleModelForm(instance=responsible)
    if request.method == "POST":
        form = ResponsibleModelForm(request.POST, instance=responsible)
        if form.is_valid():
            form.save()
            return redirect('/projects/responsibles/')
    context = {
        "form": form,
        "responsible": responsible,
    }
    return render(request, "projectResponsibles/responsible_update.html", context)

# delete view
def responsible_delete(request, pk):
    responsible = ProjectResponsible.objects.get(id=pk)
    responsible.delete()
    return redirect('/projects/responsibles/')
