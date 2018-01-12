from django.contrib import admin


class CardEffectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_affected', 'nb_dmg')
    list_filter = ['nb_dmg', 'type_affected']
    ordering = ['name']