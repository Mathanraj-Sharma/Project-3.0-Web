from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from reviews.models import review
from complaint.models import complaint
from question.models import question
from mobileusers.models import mobileuser
from hotel.models import hotel
import re, ast
import pandas as pd

# Create your views here.

def index(request):
    review_count = review.objects.all().count()
    complaint_count = complaint.objects.all().count()
    question_count = question.objects.all().count()
    mobileusers_count = mobileuser.objects.all().count()
        
    markers = get_markers()

    #get_review_score(review.objects.filter(id=1))
    #get_hotel_reviews(1)
    get_total_review_score(1)
    # print()

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
        return render(request, "login2.html")


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
    data = ast.literal_eval(review.values('qa')[0]['qa'])
    for value in data:
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

    # print(f"Score = {score}")
    return score


def get_total_review_score(hotel_id):
    """
        This function gets and hotel id as input and returns total review score
    """
    total = 0
    reviews = review.objects.filter(hotel = hotel_id).values('id')
    
    for i in reviews:
        total = total + get_review_score(review.objects.filter(id = i['id']))
       
    expected_total = len(reviews) * 35
    score = (total/expected_total) * 5

    # print(score)
    return score

def get_markers():
    """
        This function will return the list of markers for all hotels in review table
    """
    hotels = list(set([i['hotel'] for i in review.objects.all().values('hotel')]))
    # print(f'hotels{hotels}')
    markers = []
    for hotel_id in hotels:
        # lng = float(hotel.objects.filter(id = hotel_id).values('longtitude')[0]['longtitude'])
        # lat = float(hotel.objects.filter(id = hotel_id).values('latitude')[0]['latitude'])
        latlng = ast.literal_eval(hotel.objects.filter(id = hotel_id).values('geo_tag')[0]['geo_tag'])
        lng = latlng['longitude']
        lat = latlng['latitude']
        markers.append([lng, lat])
        
    return markers




