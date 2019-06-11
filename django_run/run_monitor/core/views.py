from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run
from django.urls import reverse
#from django.core.urlresolvers import reverse
# Create your views here.
def home(request):
    return render(request, 'base.html', {})


class RunList(ListView): 
    model = Run


class RunCreate (CreateView):
    model = Run
    fields = '__all__'
 
    def get_success_url(self):
       return reverse('run_list')

class RunView(DetailView):
    model = Run


class RunUpdate(UpdateView):
    model = Run
    fields = ['id_run', 'run_date', 'run_date', 'total_time', 'distance']

    def get_success_url(self):
        return reverse('run_list')

class RunDelete (DeleteView):
    model = Run
 
    def get_success_url(self):
       return reverse('run_list')


