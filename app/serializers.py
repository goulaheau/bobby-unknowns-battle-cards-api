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
            'strength',
            'effect'
        ]


class CardValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardValue
        fields = [
            'id',
            'user',
            'card',
            'health',
            'strength'
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
            'owner_mana',
            'opponent_mana',
            'player_turn',
            'owner_deck_cards',
            'opponent_deck_cards',
            'owner_hand_cards',
            'opponent_hand_cards',
            'owner_board_cards',
            'opponent_board_cards',
            'owner_graveyard_cards',
            'opponent_graveyard_cards',
            'owner',
            'opponent',
            'owner_deck',
            'opponent_deck',
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


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
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