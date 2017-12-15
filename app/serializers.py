from app.models import Deck, User, Card, Game
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'name',
            'cost',
            'picture',
            'type',
            'health',
            'strengh',
            'effect'
        ]


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = [
            'id',
            'name',
            'cards',
            'user'
        ]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'users'
        ]
