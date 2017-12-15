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


class Card(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=1)
    picture = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(CardType, on_delete=models.CASCADE, default=1)
    health = models.IntegerField(null=True)
    strengh = models.IntegerField(null=True)
    effect = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    def __str__(self):
        return self.username


class Deck(models.Model):
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(Card)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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


class Game(models.Model):
    users = models.ManyToManyField(User)
