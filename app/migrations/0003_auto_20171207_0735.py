# Generated by Django 2.0 on 2017-12-07 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171201_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='cards',
        ),
        migrations.RemoveField(
            model_name='player',
            name='current_deck',
        ),
        migrations.DeleteModel(
            name='Deck',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
