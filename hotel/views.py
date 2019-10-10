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


def hotel_list_view(request,id):
    hotel_detail = hotel.objects.all()
    hotelspecific = id
    s, d = get_total_score_doughnut(id)
    q_script, q_div = get_question_pie(id, "How good was the outside environment of the restaurant?")
    context = {
        'id': hotelspecific,
        'hotel_detail': hotel_detail,
        's' : s,
        'd' : d,
        'q_script': q_script,
        'q_div': q_div
    }
    return render(request,'hotelview.html',context)

