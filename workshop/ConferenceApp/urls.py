from django.urls import path
from .views import *
#from . import views 
urlpatterns =[
    #this is from personal function
    #path ("liste/",views.all_conferences,name="conference_liste"),
    
    
    #this is from predefined function
    path ("liste/",ConferenceList.as_view(),name="conference_liste"),
    path ("details/<int:pk>",conferenceDetails.as_view(),name="conference_details"),#we have to pass the primary key to see the details of a specific conference
]