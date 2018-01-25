from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=1)
    picture = models.ImageField(
        upload_to='card_images',
        default='media/default.png'
    )
    type = models.ForeignKey('CardType', on_delete=models.CASCADE, default=1)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    effect = models.ForeignKey(
        'CardEffect',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
