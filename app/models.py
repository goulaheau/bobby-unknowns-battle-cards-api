from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=50)
    cost  = models.IntegerField(default = 1)

class Deck(models.Model):
    name = models.CharField(max_length=50)
    cards = models.ForeignKey(Card)

class Player(models.Model):
    name = models.CharField(max_length=5)
    health = models.IntegerField(default = 30)
    current_deck = models.ForeignKey(Deck)
    mana_cristals = models.IntegerField(default = 1)

class MonsterCard(Card):
    health = models.IntegerField(default = 1)
    strengh  = models.IntegerField(default = 1)

class SpellCard(Card):
    effect = models.CharField(max_length = 100)
