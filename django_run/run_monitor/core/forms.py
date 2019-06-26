from django import forms
from .models import Run

from datetime import datetime

class RunForm(forms.ModelForm):
    created_dateField = forms.DateTimeField(
    initial=datetime.now().strftime('%m-%d-%y %H:%M'), label = 'Data da corrida',
    widget = forms.TextInput( attrs={'class':'form-control'}))
    
    run_dateField = forms.DateTimeField(initial=datetime.now().strftime('%m-%d-%y %H:%M'), label = 'Data do registro ',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    time_dateField = forms.TimeField(label = 'Tempo total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    distance_Field = forms.FloatField(label = 'Distancia total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    class Meta:
        model = Run
        fields = ['created_dateField', 'run_dateField', 'time_dateField', 'distance_Field']
