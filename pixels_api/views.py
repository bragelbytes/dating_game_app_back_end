#from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .serializers import GamesSerializer
from .models import User
from .models import Games

# Create your views here.
#User views=================
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

#Games views=================
class GamesList(generics.ListCreateAPIView):
    queryset = Games.objects.all().order_by('id')
    serializer_class = GamesSerializer

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all().order_by('id')
    serializer_class = GamesSerializer
