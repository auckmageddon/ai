from django.db import models
from schedule.models import Event

class Tournament(models.Model):
    game          = models.CharField(max_length=255)
    name          = models.CharField(max_length=255)
    challonge_url = models.URLField()
    winner        = models.CharField(max_length=255)

    scheduled_for = models.ForeignKey(Event)
