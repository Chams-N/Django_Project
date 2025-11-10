
from django import forms
from .models import Conference

class ConferenceModel(forms.ModelForm):
    class Meta:   #specify the model to be used
        model = Conference
        fields = ['name', 'theme' ,'description', 'start_date', 'end_date', 'location']
        #you can also use fields="__all__" to include all fields
        labels = {
            'name': 'Conference Name',
            'theme': 'Conference Theme',
            'description': 'Description',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'location': 'Location',
        }
        
        widgets = {
            'start_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'Select a date'
                    
                }),
            'end_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'Select a date'
                }),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Exemple: International Conference on AI'
                }),
        }