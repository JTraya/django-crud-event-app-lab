from django import forms
from .models import Moment

class MomentForm(forms.ModelForm):
    class Meta:
        model = Moment
        fields = ['name', 'date_time']
        widgets = {
            'date_time': forms.DateInput(
                format=('%Y/%m/%d'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
            )
        }