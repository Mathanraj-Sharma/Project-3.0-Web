from django.shortcuts import render, get_object_or_404,redirect
#from django.views.generic.detail import DetailView
from django.views.generic import ListView,TemplateView
from .models import hotel
from django.contrib.auth.models import User, auth
from reviews.models import review
from complaint.models import complaint
from question.models import question
from mobileusers.models import mobileuser


def hotel_list_view(request,id):
        hotel_detail = hotel.objects.all()
        hotelspecific = id
        context = {
            'id': hotelspecific,
            'hotel_detail': hotel_detail
        }
        return render(request,'hotelview.html',context)