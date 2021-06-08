from django.db import models
from django.db.models.deletion import SET_NULL

from projectTypes.models import ProjectType
from projectResponsibles.models import ProjectResponsible


# Create your models here.
class Project(models.Model):
    project_type = models.ForeignKey(
        "projectTypes.ProjectType", 
        on_delete=SET_NULL, 
        null=True,
        verbose_name='Project Type',
        help_text='choose the type of project (Dx, SpotID, etc.)')
    project_responsible = models.ForeignKey(
        "projectResponsibles.ProjectResponsible", 
        on_delete=SET_NULL, 
        null=True,
        verbose_name='Project Responsible',
        help_text='choose the person who is responsible for this project')
    code = models.CharField(max_length=10, verbose_name='Project Code')
    name = models.CharField(max_length=50, verbose_name='Project Name')
    description = models.CharField(max_length=100, verbose_name='Project Description')
    active = models.BooleanField(default=True, help_text='is the project still active, or not')

    def __str__(self):
        return f"{self.code} - {self.name}"

