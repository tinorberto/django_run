from django import forms
from .models import Run
from .models import RunSteps

from datetime import datetime

"""
Quando nao existe o model, usamos o forms.Form
widget : objeto para ser renderizado

forms.is_valid()
quando passa dele form que ele gera 
form. campo nao funciona

forms.erros.message  mesagem 
cleaned_data campo ja valido

"""
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


    run = forms.IntegerField(label = 'ID') 
    class Meta:
        model = RunSteps
        fields = ('km', 'time' , 'run')

    
    
    def __init__(self, *args, **kwargs):
        print ("---__init__-----")
        self.run = kwargs.pop('run', None)
        print (self.run)
        super(RunStepsForm, self).__init__(*args, **kwargs)
    
        #print (type(kwargs.keys()))   
    
        
        #print (kwargs['initial']['run'])
        #print (self.fields)
        print (self.fields)
        self.fields['run'].initial = self.run
        #forms.ModelForm.__init__(self, *args, **kwargs)