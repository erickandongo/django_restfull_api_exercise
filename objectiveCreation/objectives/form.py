from django import forms
from django.forms import ModelForm
from .models import Objective
from django.utils import timezone

class ObjectiveForm(ModelForm):
    class Meta:
        model = Objective
        fields = ['objective_name', 'action_phrase', 'number', 'units', 'deadline', 'objective_type',
                  'priority', 'complexity',  'start_date', 'end_date', 'definition_of_good']
        

        widgets = {
            # format='%Y-%m-%d',
            'deadline': forms.DateInput(attrs={'class': 'form-control italic-placeholder deadline-input', 'placeholder': 'Deadline', 'type': 'date'}),

            
            'start_date': forms.DateInput(attrs={'class': ' start-date form-control form-control-lg italic-placeholder', 'placeholder': 'Select a '
                                                 'date',
                                                 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'end-date-input form-control form-control-lg italic-placeholder', 'placeholder': 'Select a '
                                               'date',
                                               'type': 'date'})
         }