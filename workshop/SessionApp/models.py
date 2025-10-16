from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# OR from ConferenceApp.models import Conference
# Create your models here.

room_validator = RegexValidator(r'^[a-zA-Z0-9]+$', 'Only alphanumeric characters are allowed.')

class Session(models.Model):
    
    
    session_id=models.AutoField(primary_key=True,editable=False)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=255)
    session_day=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.CharField(max_length=255,validators=[room_validator])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    conference_id=models.ForeignKey('ConferenceApp.Conference',on_delete=models.CASCADE,related_name='sessions')
    # OR conference_id = models.ForeignKey(Conference)
    
    def date_validation(self):
        #Checks session_day belongs to the conference date range
        if self.conference_id:
            start = self.conference_id.start_date
            end = self.conference_id.end_date
            if not (start <= self.session_day <= end):
                raise ValidationError({
                    'session_day': f"Session day must be between {start} and {end}."
                })
    def start_end_time_validation(self):
        #Checks start_time is before end_time
        if self.start_time >= self.end_time:
            raise ValidationError({
                'end_time': "End time must be after start time."
            })
        
    

    def clean(self):
        self.date_validation()
        self.start_end_time_validation()

    def __str__(self):
        return self.title