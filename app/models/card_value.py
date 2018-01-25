from django.db import models


class CardValue(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    card = models.ForeignKey(
        'Card',
        on_delete=models.CASCADE,
    )
    health = models.IntegerField()
    strength = models.IntegerField()

    class Meta:
        db_table = 'app_card_value'
