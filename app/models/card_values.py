from django.db import models


class CardValues(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    card = models.ForeignKey(
        'Card',
        on_delete=models.CASCADE,
    )
    health = models.IntegerField()
    strengh = models.IntegerField()

    class Meta:
        db_table = 'app_card_values'
