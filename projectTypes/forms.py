from django import forms
from .models import ProjectType

class TypeModelForm(forms.ModelForm):
    class Meta:
        model = ProjectType
        fields = (
            'code',
            'description'
        )
