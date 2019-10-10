from django.urls import path
from . import views

urlpatterns = [
    #path('about/',views.hotel_list_view, name='hotellist')
    path('hotel/<int:id>/',views.hotel_list_view, name = 'hotelspecific')
    #path('about/', HotelView.as_view()),
]

