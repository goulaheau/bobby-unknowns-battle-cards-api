from app.models import *
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


class CardEffectSerializer(serializers.ModelSerializer):
        class Meta:
            model = CardEffect
            fields = [
                'id',
                'name',
                'type_affected',
                'nb_max_affectCard',
                'nb_affect_turn',
                'nb_dmg'
            ]

class CardTypeSerializer(serializers.ModelSerializer):
        class Meta:
            model = CardType
            fields = [
                'id',
                'name'
            ]

class GameLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameLog
        fields = [
            'winner',
            'loser'
            'nb_round'
            'start_game'
            'end_game'
        ]

class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = [
            'name',
            'card_to_pick',
            'put_card_on'
            'max_cards_on_bord'
            'max_attack_card_per_round'
            'health_pts_to_loose'
            'nb_max_cards_per_deck'
            'nb_pv_player'
        ]