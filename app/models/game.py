from django.db import models


class Game(models.Model):
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
    owner_mana = models.IntegerField(null=True)
    opponent_mana = models.IntegerField(null=True)
    player_turn = models.ForeignKey(
        'User',
        related_name='player_turn',
        on_delete=models.CASCADE,
        null=True
    )
    owner_deck_cards = models.ManyToManyField(
        'Card',
        related_name='owner_deck_cards',
        null=True
    )
    opponent_deck_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_deck_cards',
        null=True
    )
    owner_hand_cards = models.ManyToManyField(
        'Card',
        related_name='owner_hand_cards',
        null=True
    )
    opponent_hand_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_hand_cards',
        null=True
    )
    owner_board_cards = models.ManyToManyField(
        'Card',
        related_name='owner_board_cards',
        null=True
    )
    opponent_board_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_board_cards',
        null=True
    )
    owner_graveyard_cards = models.ManyToManyField(
        'Card',
        related_name='owner_graveyard_cards',
        null=True
    )
    opponent_graveyard_cards = models.ManyToManyField(
        'Card',
        related_name='opponent_graveyard_cards',
        null=True
    )

    def __str__(self):
        return self.id

