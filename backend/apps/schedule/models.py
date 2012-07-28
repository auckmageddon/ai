from django.db import models

class Event(models.Model):
    name           = models.CharField(max_length=255)
    happening_at   = models.DateTimeField()

    is_publishable = models.BooleanField()
    is_published   = models.BooleanField()