from django.db import models


class CardEffect(models.Model):
    name = models.CharField(max_length=50)
    type_affected = models.ForeignKey('CardType', on_delete=models.CASCADE, default=1)
    nb_max_card_affected = models.IntegerField()
    nb_turn_duration_of_effect = models.IntegerField()
    nb_dmg = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_card_effect'
