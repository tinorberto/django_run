from django import forms
from .models import Run
from .models import RunSteps

from datetime import datetime

class RunForm(forms.ModelForm):
    created_date = forms.DateTimeField(
    label = 'Data da corrida',
    widget = forms.TextInput( attrs={'class':'form-control'}))
    
    run_date = forms.DateTimeField( label = 'Data do registro ',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    total_time = forms.TimeField(label = 'Tempo total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    distance = forms.FloatField(label = 'Distancia total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    class Meta:
        model = Run
        fields = ('created_date', 'run_date', 'total_time', 'distance')

'''     
    def clean(self):
'''


class RunStepsForm(forms.ModelForm):
    km = forms.IntegerField(label = 'Km parcial :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    time = forms.TimeField(label = 'Tempo total :',
    widget = forms.TextInput( attrs={'class':'form-control'})) 


    run = forms.IntegerField(widget=forms.HiddenInput()) 
    class Meta:
        model = RunSteps
        fields = ('km', 'time' )

    def __init__(self, *args, **kwargs):
         super(RunStepsForm, self).__init__(*args, **kwargs)
         print (args)
         print (self.fields)
