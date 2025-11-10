from django.shortcuts import render
from .models import Conference , Submission
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ConferenceModel
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
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
    
    
class ConferenceCreateView(LoginRequiredMixin,CreateView):
    model = Conference
    template_name = 'Conferences/conference_form.html'
    form_class =ConferenceModel
    #fields = "__all__"
    success_url = reverse_lazy('conference_liste')    #redirect to conference list after successful creation
    
    
class ConferenceUpdateView(LoginRequiredMixin,UpdateView):
    model = Conference
    template_name = 'Conferences/conference_form.html'
    form_class =ConferenceModel
    #fields = "__all__"
    success_url = reverse_lazy('conference_liste')    #redirect to conference list after successful update
    
class ConferenceDeleteView(LoginRequiredMixin,DeleteView):
    model = Conference
    template_name = 'Conferences/conference_confirm_delete.html' #default is <app_name>/<model_name>_confirm_delete.html
    success_url = reverse_lazy('conference_liste')    #redirect to conference list after successful deletion
    
    

#this is another personal function
def all_submissions(request):
    submissions=Submission.objects.all()
    return render(request,'Submissions/liste.html',{'liste':submissions})



#we are going to use predefined functions
class SubmissionList(ListView):
    model= Submission
    context_object_name = 'liste'
    ordering = ['-submission_date']  #ordering by submission_date descending
    #you have to call the template by this name <app_name>/<model_name>_list.html
    template_name = 'Submissions/liste.html'

    def get_queryset(self):
        #show the only submissions of the logged-in user
        return Submission.objects.filter(user_id=self.request.user)
    
    
class submissionDetails(DetailView):
    model= Submission
    context_object_name = 'submission'
    ordering = ['-submission_date']  #ordering by submission_date descending
    #you have to call the template by this name <app_name>/<model_name>_list.html
    template_name = 'Submissions/details.html'
    
class SubmissionCreateView(LoginRequiredMixin,CreateView):
    model = Submission
    template_name = 'Submissions/submission_form.html'
    fields = ['title','abstract','keywords','paper','conference_id']
    success_url = reverse_lazy('submission_liste')    #redirect to submission list after successful creation

    def form_valid(self, form):
        form.instance.user_id_id = self.request.user  #set the user_id to the logged-in user
        return super().form_valid(form)
    
class SubmissionUpdateView(LoginRequiredMixin,UpdateView):
    model = Submission
    template_name = 'Submissions/submission_form.html'
    fields = ['title','abstract','keywords','paper','conference_id']
    success_url = reverse_lazy('submission_liste')    #redirect to submission list after successful update
    def dispatch(self, request, *args, **kwargs):  #to restrict update to the owner only
        submission = self.get_object()
        if submission.user_id_id != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)