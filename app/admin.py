from app.models import *

# Register your models here.
admin.site.register(Deck, DeckAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardEffect, CardEffectAdmin)
admin.site.register(CardType)