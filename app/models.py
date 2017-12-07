from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length = 50)
    cost = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length = 50)
    cards = models.ForeignKey(Card, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length = 5)
    health = models.IntegerField(default = 30)
    current_deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    mana_cristals = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

class MonsterCard(Card):
    health = models.IntegerField(default = 1)
    strengh  = models.IntegerField(default = 1)

class SpellCard(Card):
    effect = models.CharField(max_length = 100)
