from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import City, Author, Article
#from .forms import

#---------------------ADMIN---------------------------

def signup(request):
    error_message=''

    if request.method == 'POST':
        user_form = UserCreationForm(data = {'username':request.POST['username'], 'password1': request.POST['password1'], 'password2': request.POST['password2']})
        if user_form.is_valid():
            user = user_form.save()
            new_form.user_id = user.id 

            login(request, user)
        return redirect('', home) #needs to change to profile when made

def home (request):
    return render(request, 'home.html')