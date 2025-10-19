from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.

#this is a personal function
def all_conferences(request):
    conferences=Conference.objects.all()
    return render(request,'Conferences/liste.html',{'liste':conferences})


#we are going to use predefined functions
class ConferenceList(ListView):
    model= Conference
    context_object_name = 'liste'
    ordering = ['-start_date']  #ordering by start_date descending
    #you have to call the template by this name <app_name>/<model_name>_list.html
    template_name = 'Conferences/liste.html'
    
class conferenceDetails(DetailView):
    model= Conference
    context_object_name = 'conference'
    ordering = ['-start_date']  #ordering by start_date descending
    #you have to call the template by this name <app_name>/<model_name>_list.html
    template_name = 'Conferences/details.html'