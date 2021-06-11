from django import forms

class ResponsibleForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
