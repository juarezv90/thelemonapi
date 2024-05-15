from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu
from rest_framework.permissions import IsAuthenticated
from .forms import BookingForm
from datetime import datetime
from django.core import serializers
import json
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class BookingViews(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class SingleBookingView(generics.RetrieveDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu = Menu.objects.get(pk=pk) 
    else: 
        menu = "" 
    return render(request, 'menu_item.html', {"menu": menu}) 


@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(booking_date=data['reservation_date']).filter(
            time_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                name=data['first_name'],
                booking_date=data['reservation_date'],
                time_slot=data['reservation_slot'],
                no_of_guest=data['reservation_count'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date', datetime.today().date())

    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')