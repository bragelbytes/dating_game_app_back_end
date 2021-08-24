#from django.shortcuts import render
from rest_framework import generics
from .serializers import UserAccountSerializer
from .serializers import GamesSerializer
from .models import UserAccount
from .models import Games

from django.contrib.auth.hashers import make_password, check_password

from django.http import JsonResponse

import json



# Create your views here.
#User views=================
class UserList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer
def check_login(request):

    if request.method=='GET':
        return JsonResponse({})

    if request.method=="PUT":
        
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        password = jsonRequest['password']
        if UserAccount.objects.get(username=username):
            user = UserAccount.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'username': user.username,'age': user.age,'name': user.name,'fav_console': user.fav_console, 'image': user.image,})
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})

#Games views=================
class GamesList(generics.ListCreateAPIView):
    queryset = Games.objects.all().order_by('id')
    serializer_class = GamesSerializer

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all().order_by('id')
    serializer_class = GamesSerializer
