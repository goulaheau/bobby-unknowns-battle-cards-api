from app.models import Deck, Player, Card
from rest_framework import serializers


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('name', 'cards')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id','name', 'health', 'current_deck', 'mana_cristals')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id','name', 'cost', 'picture', 'type', 'health', 'strengh', 'effect')
