from django.contrib import admin


class GameLogAdmin(admin.ModelAdmin):
    list_display = ['winner', 'loser', 'nb_round', 'start_game', 'end_game']
    list_filter = ['winner', 'loser']
    ordering = ['winner']

