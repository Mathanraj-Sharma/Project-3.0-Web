from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from reviews.models import review
from complaint.models import complaint
from question.models import question
from mobileusers.models import mobileuser

# Create your views here.

def index(request):
    return render(request, "index2.html")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username= username, password = password)
        review_count = review.objects.all().count()
        complaint_count = complaint.objects.all().count()
        question_count = question.objects.all().count()
        mobileusers_count = mobileuser.objects.all().count()

        context = {
            'review_count': review_count,
            'complaint_count': complaint_count,
            'question_count': question_count,
            'mobileusers_count': mobileusers_count
        }
        
        if user is not None:
            auth.login(request, user)
            return render(request,'index2.html', context)
        else: 
            #messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')