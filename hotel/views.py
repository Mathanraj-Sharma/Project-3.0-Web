from django.shortcuts import render, get_object_or_404,redirect
#from django.views.generic.detail import DetailView
from django.views.generic import ListView,TemplateView
from .models import hotel
from django.contrib.auth.models import User, auth
from reviews.models import review
from complaint.models import complaint
from question.models import question
from mobileusers.models import mobileuser
from graph.views import get_total_score_doughnut, get_question_pie
import ast


def hotel_list_view(request,id):
    hotel_detail = hotel.objects.all()
    hotelspecific = id
    marker = get_marker(id)
    overall_script, overall_div = get_total_score_doughnut(id)
    q_script, q_div = get_question_pie(id, "How good was the outside environment of the restaurant?")
    context = {
        'id': hotelspecific,
        'hotel_detail': hotel_detail,
        'marker' : marker,
        'overall_script' : overall_script,
        'overall_div' : overall_div,
        'q_script': q_script,
        'q_div': q_div
    }
    return render(request,'hotelview.html',context)

def get_marker(hotel_id):
    """
        This function will return the list of markers for all hotels in review table
    """
    marker = []
    latlng = ast.literal_eval(hotel.objects.filter(id = hotel_id).values('geo_tag')[0]['geo_tag'])
    marker.append(latlng['longitude'])
    marker.append(latlng['latitude'])
        
    return marker