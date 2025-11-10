from django.urls import path
from .views import *
#from . import views 
urlpatterns =[
    #this is from personal function
    #path ("liste/",views.all_conferences,name="conference_liste"),
    
    
    #this is from predefined function
    path ("liste/",ConferenceList.as_view(),name="conference_liste"),  #you check it in the views.py
    path ("details/<int:pk>",conferenceDetails.as_view(),name="conference_details"),#we have to pass the primary key to see the details of a specific conference
    path('form/',ConferenceCreateView.as_view(),name="conference_add"), #to create a new conference
    path('edit/<int:pk>/',ConferenceUpdateView.as_view(),name="conference_edit"), #to update a conference
    path('<int:pk>/delete/',ConferenceDeleteView.as_view(),name="conference_delete"), #to delete a conference
    
    
    path ("submissions/",SubmissionList.as_view(),name="submission_liste"),  #you check it in the views.py
    path ("submission/details/<int:pk>",submissionDetails.as_view(),name="submission_details"),#we have to pass the primary key to see the details of a specific submission
    path('submission/form/',SubmissionCreateView.as_view(),name="submission_add"), #to create a new submission
    path('submission/edit/<int:pk>/',SubmissionUpdateView.as_view(),name="submission_edit"), #to update a submission
]