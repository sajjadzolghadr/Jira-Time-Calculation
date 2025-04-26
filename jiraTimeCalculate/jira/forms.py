from django import forms
from .models import UploadedFile

class UploadCSVForm(forms.Form):
    file = forms.FileField()
