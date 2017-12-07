from django.contrib import admin
from app.models import Deck,Player,MonsterCard,SpellCard

# Register your models here.
admin.site.register(Deck);
admin.site.register(Player);
admin.site.register(MonsterCard);
admin.site.register(SpellCard);