from django.db import models


class Rule(models.Model):
    name = models.CharField(max_length=50)
    card_to_pick = models.IntegerField(default=1)
    put_card_on = models.IntegerField(default=0)
    max_cards_on_bord = models.IntegerField(default=3)
    max_attack_card_per_round = models.IntegerField(default=3)
    health_pts_to_loose = models.IntegerField(default=0)
    nb_max_cards_per_deck = models.IntegerField(default=30)
    nb_pv_player = models.IntegerField(default=30)