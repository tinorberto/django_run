from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run
from .models import RunSteps
from .forms import RunForm
from .forms import RunStepsForm
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
#from django.core.urlresolvers import reverse
# Create your views here.
def home(request):
    return render(request, 'base.html', {})


class RunList(ListView): 
    model = Run


class RunCreate (CreateView):
    model = Run
    form_class = RunForm
 
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

class RunStepsCreate (CreateView):
    model = RunSteps
    form_class = RunStepsForm 


    
    def get_context_data(self, **kwargs):
        "data = super().get_context_data(**kwargs)"
        data = context_data = super(RunStepsCreate, self).get_context_data(**kwargs)
        print ("get_context_data")
        print (type(data["form"].fields))
        print ((data["form"].fields["run"].widget))
        run = get_object_or_404(Run, id_run=self.kwargs.get('id_run'))
        data['run'] = run
        print (run)
        return data 

    '''
    get_object_or_404 - Ccaso nao retorne lancar um 404
    '''
    '''
    def get_initial(self):
        print (self.kwargs.get('id_run'))
        run = get_object_or_404(Run, id_run=self.kwargs.get('id_run'))
        return {
            'run' : run
        }

    '''
    def get_success_url(self):
       return reverse('run_list')