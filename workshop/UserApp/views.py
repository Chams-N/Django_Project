from django.shortcuts import render
from .forms import userForm
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userForm(request.POST) #get all the data from the form
        if form.is_valid():  #check if the data is valid
            form.save()  #save the data to the database
            return redirect("login")#redirect to the login page if successful
    else:
        form = userForm()
    return render(request, 'Users/register.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')