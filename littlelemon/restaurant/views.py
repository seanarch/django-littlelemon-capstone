from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuSerializer, BookingSerializer 
from .models import Menu, Booking


# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer 

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
 
class BookingViewSet(ModelViewSet): 
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer

    permission_classes = [IsAuthenticated]