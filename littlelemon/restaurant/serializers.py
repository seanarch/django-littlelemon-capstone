from django.contrib.auth.models import User 
from rest_framework import serializers 
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Menu 
        fields = ['title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Booking
        fields = ['name', 'no_of_gests', 'bookingdate'] 
        