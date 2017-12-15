from app.models import *


admin.site.register(Deck)
admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(CardType)