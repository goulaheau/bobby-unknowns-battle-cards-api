from app.models import Deck, User, Card
from rest_framework import serializers


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = (
            'name',
            'cards'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'decks'
        )


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id',
            'name',
            'cost',
            'picture',
            'type',
            'health',
            'strengh',
            'effect'
        )
