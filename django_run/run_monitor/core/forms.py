from django import forms
from .models import Run

from datetime import datetime

class RunForm(forms.ModelForm):
    created_date = forms.DateTimeField(
    initial=datetime.now().strftime('%m-%d-%y %H:%M'), label = 'Data da corrida',
    widget = forms.TextInput( attrs={'class':'form-control'}))
    
    run_date = forms.DateTimeField(initial=datetime.now().strftime('%m-%d-%y %H:%M'), label = 'Data do registro ',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    total_time = forms.TimeField(label = 'Tempo total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    distance = forms.FloatField(label = 'Distancia total :',
    widget = forms.TextInput( attrs={'class':'form-control'}))

    class Meta:
        model = Run
        fields = ('created_date', 'run_date', 'total_time', 'distance')


    def clean_distance(self): 
        print (self.cleaned_data['distance'])
        data = 5
        self.cleaned_data['distance'] = 2
        return  self.cleaned_data['distance']


    def clean(self):
        print (self.clean)
        cleaned_data=super(RunForm, self).clean()
        print(cleaned_data)

    def clean_created_date(self): 
        print (self.cleaned_data['created_date'])
        return self.cleaned_data['created_date']