from django import forms

class RunForm(forms.Form):
    run_date = forms.DateTimeField(help_text="Enter a date between now and 4 weeks (default 3).")
    created_date = forms.DateTimeField(help_text="Enter a date between now and 4 weeks (default 3).")
    total_time = forms.CharField(help_text="Enter a date between now and 4 weeks (default 3).")
    distance = forms.FloatField(help_text="Enter a date between now and 4 weeks (default 3).")
