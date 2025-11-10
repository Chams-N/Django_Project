from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator #to validate first name and last name
import uuid
#creating method to generate user_id
def generate_user_id():
    return 'USER' + uuid.uuid4().hex[:4].upper() #uuid generates random unique id example USER1A2B

def verify_email(email):
    domain = ["esprit.tn","tek.tn","sesame.com","centrale.com"]
    if email.split('@')[-1] not in domain:
        raise ValidationError('Invalid email domain.It should be one of the following: ' + ', '.join(domain))
#to validate first name and last name
name_validator = RegexValidator(r'^[a-zA-Z\s-]+$', 'Only alphabetic characters, spaces, and hyphens (-) are allowed.')
#mot clef r + chaine de caractere ,espaces (s) et tirets autorises ()



#model is a blue print of a database table
#we need class models.Model to create a model
#if i wnat to use my proper class model instead of the default user model abstractuser
class UserModel(models.Model): 
    pass
# Create your models here.
class User(AbstractUser):
    user_id=models.CharField(max_length=10,primary_key=True,unique=True,editable=False)
    first_name=models.CharField(max_length=50,validators=[name_validator]) #to validate first name
    last_name=models.CharField(max_length=50,validators=[name_validator]) #to validate last name
    affiliation=models.CharField(max_length=255)
    ROLE=[
        ("Participant","Participant"),
        ("Commitee","Organizing Commitee Member"),
        ]
    role=models.CharField(max_length=255,choices=ROLE,default="Participant")
    nationality=models.CharField(max_length=50)
    email=models.EmailField(unique=True,validators=[verify_email])#to validate email domain
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs): #args are positional arguments, kwargs are keyword arguments
        if not self.user_id:
            new_id = generate_user_id()
            while User.objects.filter(user_id=new_id).exists():
                new_id = generate_user_id() #generate new id if it already exists
            self.user_id = new_id
        super().save(*args, **kwargs) #call the save method of the parent class
        #super().save() #call the save method of the parent classes
        
    #another way to create many to many relationship:
    #submissions=models.ManyToManyField('ConferenceApp.Conference',through='Submission',related_name='submissions')
    #OrganizingCommitteeLst=models.ManyToManyField('ConferenceApp.Conference',through='OrganizingCommittee',related_name='organizing_committees')
    
    
class OrganizingCommittee(models.Model):
    
    user_id=models.ForeignKey('UserApp.User',on_delete=models.CASCADE,related_name='committees')
    conference_id=models.ForeignKey('ConferenceApp.Conference',on_delete=models.CASCADE,related_name='committees')
    ROLES=[
        ("Chair","Chair"),
        ("Co-Chair","Co-Chair"),
        ("Member","Member"),
    ]
    committee_role=models.CharField(max_length=255,choices=ROLES,default="Member")
    date_joined=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    