from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run
from .models import RunSteps
from .forms import RunForm
from django.urls import reverse
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

    def form_invalid(self,form):
        # Add action to invalid form phase
        print ("-------")
        messages.success(self.request, 'An error occured while processing the payment')
        return self.render_to_response(self.get_context_data(form=form)) 

    def form_valid(self, form):
        print ('-OOOOOOOOOOOOOO--')
        print (model.created_date)
        model.created_date = model.created_date.strftime("%YYYY-%MM-%DD %HH:%MM:%SS.SSS")
        print (model.created_date)
        model = form.save(commit=False)
        model.submitted_by = self.request.user
        model.save()
        return HttpResponseRedirect(self.get_success_url())

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
    fields = '__all__'
    def get_success_url(self):
       return reverse('run_list')
    
    def form_valid(self, form):
        pirnt ('---')
        print (model.created_date)
        model.created_date = model.created_date.strftime("%YYYY-%MM-%DD %HH:%MM:%SS.SSS")
        print (model.created_date)
        model = form.save(commit=False)
        model.submitted_by = self.request.user
        model.save()
        return HttpResponseRedirect(self.get_success_url())