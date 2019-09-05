from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from reviews.models import review
from complaint.models import complaint
from question.models import question
from mobileusers.models import mobileuser
import re

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
        
        review_geo_list = review.objects.values('geo_tag')
        markers = []
        for i  in review_geo_list:
            y = i.get('geo_tag')
            markers.append([float(s) for s in re.findall(r"[-+]?\d*\.\d+|\d+", y)])
        markers = [list(marker) for marker in set(tuple(row) for row in markers)]
       
        context = {
            'review_count': review_count,
            'complaint_count': complaint_count,
            'question_count': question_count,
            'mobileusers_count': mobileusers_count, 
            'markers': markers
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