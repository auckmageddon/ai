from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    title        = models.CharField(max_length=255)
    content      = models.TextField()

    is_published = models.BooleanField(default=True)
    frontpage_me = models.BooleanField(default=True)

    entered_by   = models.ForeignKey(User)
    entered_on   = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-entered_on"]


class Event(models.Model):
    name           = models.CharField(max_length=255)
    happening_at   = models.DateTimeField()

    is_publishable = models.BooleanField(default=True)
    is_published   = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s at %s" % (self.name, self.happening_at)

    class Meta:
        ordering = ["happening_at"]


class Tournament(models.Model):
    name          = models.CharField(max_length=255)
    challonge_url = models.URLField()

    scheduled_for = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]