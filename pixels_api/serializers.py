from rest_framework import serializers
from .models import UserAccount
from .models import Games

from django.contrib.auth.hashers import make_password, check_password

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'password', 'image', 'name', 'age', 'fav_console', 'fav_games',)

    ### THIS HASHES A NEW USERS PASSWORD WHEN THEY CREATE AN ACCOUNT
    def create(self, validated_data):
        user = UserAccount.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    ### THIS MAKES SURE THEIR UPDATED PASSWORDS ARE ALSO HASHED
    def update(self, instance, validated_data):
        user = UserAccount.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('name', 'image', 'genre')
