#from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
