from django.contrib import admin
from app.models import Deck, User, Card, CardType

# Register your models here.
admin.site.register(Deck)
admin.site.register(User)
admin.site.register(Card)
admin.site.register(CardType)