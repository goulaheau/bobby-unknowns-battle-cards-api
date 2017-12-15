from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib import admin


# Triggered whenever a new user has been created and saved to the DB
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CardType(models.Model):
    name = models.CharField(max_length=20, default='Monster')

    def __str__(self):
        return self.name

class CardEffect(models.Model):
    name = models.CharField(max_length=50)
    typeAffected = models.ForeignKey(CardType, on_delete=models.CASCADE, default=1)
    nbMaxAffectCard = models.IntegerField()
    nbAffectTurn = models.IntegerField()
    nbDmg = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CardEffectAdmin(admin.ModelAdmin):
    list_display = ('name',  'typeAffected', 'nbDmg')
    list_filter = ['nbDmg', 'typeAffected']
    ordering = ['name']

class Card(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='card_images',default='media/default.png')
    type = models.ForeignKey(CardType, on_delete=models.CASCADE, default=1)
    health = models.IntegerField(null=True)
    strengh = models.IntegerField(null=True)
    effect = models.ForeignKey(CardEffect, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class CardAdmin(admin.ModelAdmin):
    list_display = ('name',  'cost', 'effect')
    list_filter = ['effect', 'type', 'cost']
    ordering = ['name']


class User(AbstractUser):
    def __str__(self):
        return self.username


class Deck(models.Model):
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(Card)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_cards(self):
        return ", ".join([str(p) for p in self.cards.all()])


class DeckAdmin(admin.ModelAdmin):
    list_display = ('name',  'user', 'get_cards')
    list_filter = ['name']
    ordering = ['name']

    def author_first_name(self, obj):
        return obj.author.first_name

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'last_login', 'is_staff', 'is_active', 'is_superuser']
    list_filter = ['is_superuser', 'is_active', 'is_staff']
    ordering = ['username']

    # Personnalisation des champs du formulaire
    fieldsets = (
        ('USER', {
            'description': 'Propriétés du user',
            'fields': ['username', 'password', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active']}
         ),
        ('PLAYER', {
            'description': 'Deck(s) du joueur',
            'fields': ['decks']}
         )
    )

class gameInfos(models.Model):
    winner = models.OneToOneField(User, related_name='user_who_won', on_delete=models.CASCADE)
    loser = models.OneToOneField(User, related_name='user_who_lose', on_delete=models.CASCADE)
    nbRound = models.IntegerField()
    startGame = models.DateTimeField()
    endGame = models.DateTimeField()

    def __str__(self):
        return self.winner

class gameInfosAdmin(admin.ModelAdmin):
    list_display = ['winner', 'loser', 'nbRound', 'startGame', 'endGame']
    list_filter = ['winner', 'loser']
    ordering = ['winner']

