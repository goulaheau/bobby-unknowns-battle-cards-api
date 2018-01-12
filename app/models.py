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


class User(AbstractUser):
    def __str__(self):
        return self.username


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'last_login', 'is_staff', 'is_active',
                    'is_superuser']
    list_filter = ['is_superuser', 'is_active', 'is_staff']
    ordering = ['username']

    # Personnalisation des champs du formulaire
    fieldsets = (
        ('USER', {
            'description': 'Propriétés du user',
            'fields': ['username', 'password', 'email', 'last_login',
                       'date_joined', 'is_superuser', 'is_staff', 'is_active']}
         ),
        ('PLAYER', {
            'description': 'Deck(s) du joueur',
            'fields': ['deck']}
         )
    )


class CardType(models.Model):
    name = models.CharField(max_length=20, default='Monster')

    def __str__(self):
        return self.name


class CardEffect(models.Model):
    name = models.CharField(max_length=50)
    type_affected = models.ForeignKey(CardType, on_delete=models.CASCADE,
                                      default=1)
    nb_max_affectCard = models.IntegerField()
    nb_affect_turn = models.IntegerField()
    nb_dmg = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CardEffectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_affected', 'nb_dmg')
    list_filter = ['nb_dmg', 'type_affected']
    ordering = ['name']


class Card(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='card_images',
                                default='media/default.png')
    type = models.ForeignKey(CardType, on_delete=models.CASCADE, default=1)
    health = models.IntegerField(null=True)
    strengh = models.IntegerField(null=True)
    effect = models.ForeignKey(CardEffect, on_delete=models.CASCADE, null=True,
                               blank=True)

    def __str__(self):
        return self.name


class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'effect')
    list_filter = ['effect', 'type', 'cost']
    ordering = ['name']


class Deck(models.Model):
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(Card)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_cards(self):
        return ", ".join([str(p) for p in self.cards.all()])


class DeckAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_cards')
    list_filter = ['name']
    ordering = ['name']

    def author_first_name(self, obj):
        return obj.author.first_name


class GameLog(models.Model):
    winner = models.OneToOneField(
        User,
        related_name='user_who_won',
        on_delete=models.CASCADE
    )
    loser = models.OneToOneField(
        User,
        related_name='user_who_lose',
        on_delete=models.CASCADE
    )
    nb_round = models.IntegerField()
    start_game = models.DateTimeField()
    end_game = models.DateTimeField()
    game = models.OneToOneField(
        'Game',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.winner


class GameLogAdmin(admin.ModelAdmin):
    list_display = ['winner', 'loser', 'nb_round', 'start_game', 'end_game']
    list_filter = ['winner', 'loser']
    ordering = ['winner']


class Game(models.Model):
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
        User,
        related_name='owner',
        on_delete=models.CASCADE,
    )
    opponent = models.ForeignKey(
        User,
        related_name='opponent',
        on_delete=models.CASCADE,
        null=True,
    )

    owner_deck = models.ForeignKey(
        Deck,
        related_name='owner_deck',
        on_delete=models.CASCADE,
    )
    opponent_deck = models.ForeignKey(
        Deck,
        related_name='opponent_deck',
        on_delete=models.CASCADE,
        null=True,
    )


class ActionsLog(models.Model):
    game_log = models.ForeignKey(GameLog, on_delete=models.CASCADE)
    date = models.DateTimeField()
    tour = models.IntegerField(null=False)
    libelle = models.CharField(max_length=250)
