from app.models import *


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(CardType)
admin.site.register(CardEffect)
admin.site.register(Card)
admin.site.register(Deck)
