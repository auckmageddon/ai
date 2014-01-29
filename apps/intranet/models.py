from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
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
        return u'{} at {}'.format(self.name, self.happening_at)

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


class Profile(models.Model):
    steam_id     = models.CharField(max_length=255, unique=True)
    username     = models.CharField(max_length=255)

    avatar_url   = models.URLField()
    profile_url  = models.URLField()

    game_id      = models.CharField(max_length=255, null=True, blank=True)
    game_name    = models.CharField(max_length=255, null=True, blank=True)
    game_ip      = models.CharField(max_length=255, null=True, blank=True)

    last_updated = models.DateTimeField(auto_now=True)
