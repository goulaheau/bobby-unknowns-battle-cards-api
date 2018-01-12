from django.db import models


class Game(models.Model):
    users = models.ManyToManyField('User')
    turn = models.IntegerField(null=True)
    owner_mana = models.IntegerField(null=True)
    opponent_mana = models.IntegerField(null=True)
    owner_deck_cards = models.ManyToManyField(
        'Card',
        related_name='owner_deck_cards',
    )
    opponent_deck_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_deck_cards',
    )
    owner_hand_cards = models.ManyToManyField(
        'Card',
        related_name='owner_hand_cards',
    )
    opponent_hand_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_hand_cards',
    )
    owner_board_cards = models.ManyToManyField(
        'Card',
        related_name='owner_board_cards',
    )
    opponent_board_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_board_cards',
    )
    owner_graveyard_cards = models.ManyToManyField(
        'Card',
        related_name='owner_graveyard_cards',
    )
    opponent_graveyard_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_graveyard_cards',
    )
    owner = models.ForeignKey(
        'User',
        related_name='owner',
        on_delete=models.CASCADE,
    )
    opponent = models.ForeignKey(
        'User',
        related_name='opponent',
        on_delete=models.CASCADE,
        null=True,
    )
    owner_deck = models.ForeignKey(
        'Deck',
        related_name='owner_deck',
        on_delete=models.CASCADE,
    )
    opponent_deck = models.ForeignKey(
        'Deck',
        related_name='opponent_deck',
        on_delete=models.CASCADE,
        null=True,
    )

def __str__(self):
    return self.name

