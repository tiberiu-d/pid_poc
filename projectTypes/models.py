from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class ProjectType(models.Model):
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code} - {self.description}"
