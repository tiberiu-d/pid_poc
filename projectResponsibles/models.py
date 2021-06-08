from django.db import models

# Create your models here.
class ProjectResponsible(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    email = models.EmailField(null=True)

    def __str__(self):
        return self.full_name

