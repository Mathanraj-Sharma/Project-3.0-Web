from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    return render(request, "index2.html")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username= username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else: 
            #messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')