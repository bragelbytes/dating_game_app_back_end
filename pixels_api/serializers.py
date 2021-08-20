from rest_framework import serializers
from .models import User
from .models import Games

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'image', 'name', 'age', 'fav_console', 'fav_games',)

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('name', 'image', 'genre')
