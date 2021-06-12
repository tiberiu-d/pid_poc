from django import forms
from .models import ProjectResponsible

class ResponsibleForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()


class ResponsibleModelForm(forms.ModelForm):
    class Meta:
        model = ProjectResponsible
        fields = (
            'full_name',
            'email',
        )
