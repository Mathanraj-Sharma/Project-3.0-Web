from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from reviews.models import review
from complaint.models import complaint
from question.models import question
from mobileusers.models import mobileuser
import re

# Create your views here.

def index(request):
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

    get_review_score(review.objects.filter(id=1))

    context = {
        'review_count': review_count,
        'complaint_count': complaint_count,
        'question_count': question_count,
        'mobileusers_count': mobileusers_count, 
        'markers': markers
    }
        
    return render(request, "index2.html", context)

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username= username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
            #return render(request,'index2.html', context)
        else: 
            #messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def get_review_score(review):
    """
        This method will get a single review as input and returns the score for it
    """
    grade_A = ['Very Good', 'Very Pleasant','Very Nice','Yes', 'Very Tasty']
    grade_B = ['Good', 'Pleasant', 'Nice']
    grade_C = ['Moderate', 'Neutral']
    grade_D = ['Bad']
    grade_E = ['Worse','Very Bad','No']

    score = 0
    data = review.values('queAndAnsr')
    for value in data[0]['queAndAnsr'].values():
        temp = value['answer']
        if temp in grade_A:
            score += 5
        elif temp in grade_B:
            score += 4
        elif temp in grade_C:
            score += 3
        elif temp in grade_D:
            score += 2
        else:
            score += 0

    #print(f"Score = {score}")
    return score

