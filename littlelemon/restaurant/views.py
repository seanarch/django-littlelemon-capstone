from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuSerializer, BookingSerializer 
from .models import Menu, Booking


# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer 

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
 