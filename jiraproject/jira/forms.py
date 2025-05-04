from django import forms
from .models import UploadedFile

class UploadCSVForm(forms.Form):
    file = forms.FileField()
    monthly_work_hours = forms.IntegerField(label='Monthly Work Hours')
