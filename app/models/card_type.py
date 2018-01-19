from django.db import models


class CardType(models.Model):
    name = models.CharField(max_length=20, default='Monster')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_card_type'
