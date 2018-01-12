from django.db import models


class ActionsLog(models.Model):
    game_log = models.ForeignKey('GameLog', on_delete=models.CASCADE)
    date = models.DateTimeField()
    tour = models.IntegerField(null=False)
    libelle = models.CharField(max_length=250)