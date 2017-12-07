from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your models here.
class CardType(models.Model):
    name = models.CharField(max_length = 20, default='Monster')

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length = 50)
    cost = models.IntegerField(default = 1)
    picture = models.CharField(default=None, max_length=255, null=True)
    type = models.ForeignKey(CardType, on_delete=models.CASCADE,default=1)
    health = models.IntegerField(default=None, null=True)
    strengh = models.IntegerField(default=None, null=True)
    effect = models.CharField(max_length=100, default=None, null=True)

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
    current_deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True)
    mana_cristals = models.IntegerField(default = 1)

    def __str__(self):
        return self.name
