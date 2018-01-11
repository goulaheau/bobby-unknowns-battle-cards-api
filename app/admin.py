from app.models import *



# Register your models here.
<<<<<<< HEAD
admin.site.register(User, UserAdmin)
admin.site.register(CardType)
admin.site.register(CardEffect)
admin.site.register(Card)
admin.site.register(Deck)
=======
admin.site.register(Deck, DeckAdmin)
admin.site.register(User, UserAdmin)
# admin.site.register(User)
admin.site.register(Card, CardAdmin)
admin.site.register(CardEffect, CardEffectAdmin)
admin.site.register(CardType)
admin.site.register(GameLog, GameLogAdmin)

>>>>>>> f82567a8d9f47442be8e29928f3ed2abaaceaa85
