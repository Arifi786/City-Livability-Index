from django import forms
from .models import Arif

class ArifForm(forms.ModelForm):
    class Meta:
        model = Arif
        fields = ['field1', 'field2']  # Specify the fields you want to include in the form
