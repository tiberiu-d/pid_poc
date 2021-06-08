from django.db import models
from django.db.models.deletion import SET_NULL
from Projects.models import Project


class Link(models.Model):
    source = models.ForeignKey(
        "Projects.Project",
        related_name='source',
        null=True,
        on_delete=SET_NULL)
    destination = models.ManyToManyField(
        "Projects.Project",
        related_name='destination'
    )
