from django.db import models


class GameLog(models.Model):
    winner = models.OneToOneField(
        'User',
        related_name='user_who_won',
        on_delete=models.CASCADE
    )
    loser = models.OneToOneField(
        'User',
        related_name='user_who_lose',
        on_delete=models.CASCADE
    )
    nb_round = models.IntegerField()
    start_game = models.DateTimeField()
    end_game = models.DateTimeField()
    game = models.OneToOneField(
        'Game',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.winner

    class Meta:
        db_table = 'app_game_log'
