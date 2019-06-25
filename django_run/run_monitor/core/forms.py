from django import forms
from .models import Run

from datetime import datetime

class RunForm(forms.ModelForm):
    created_dateField = forms.DateTimeField(initial=datetime.now(), label = 'Data da corrida',
    widget = forms.TextInput( attrs={'class':'form-control'}))
    
    run_dateField = forms.DateTimeField(initial=datetime.now(), label = 'Data do registro ',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    time_dateField = forms.TimeField(label = 'Tempo total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    distance_Field = forms.FloatField(label = 'Distancia total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    class Meta:
        model = Run
        fields = ['created_dateField', 'run_dateField', 'time_dateField', 'distance_Field']



"""
    id_run = models.AutoField(primary_key=True)
    run_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField( default=timezone.now)
    total_time = models.CharField(max_length=200)
    distance = models.FloatField()
"""