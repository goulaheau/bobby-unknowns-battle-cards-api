from app.models import *

# Register your models here.
admin.site.register(Deck)
admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(CardEffect)
admin.site.register(CardType)