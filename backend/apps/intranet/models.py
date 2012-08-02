from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()

    is_published = models.BooleanField()

    entered_by = models.ForeignKey(User)
    entered_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=255)
    happening_at = models.DateTimeField()

    is_publishable = models.BooleanField()
    is_published = models.BooleanField()

    def __unicode__(self):
        return u"%s at %s" % (self.name, self.happening_at)


class Server(models.Model):
    address = models.CharField(max_length=21, unique=False)
    game = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    players = models.IntegerField()
    max_players = models.IntegerField()
    map = models.CharField(max_length=50)
    last_seen = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s at %s" % (self.game, self.address)


class Tournament(models.Model):
    game = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    challonge_url = models.URLField()
    winner = models.CharField(max_length=255)

    scheduled_for = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name


class FAQ(models.Model):
    name = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()

    def __unicode__(self):
        return self.name


class BarTab(models.Model):
    code = models.CharField(max_length=32, unique=True)
    confirmation = models.CharField(max_length=8, unique=True)
    value = models.IntegerField()

    claimed = models.BooleanField(default=False)
    claimant = models.CharField(max_length=15, default="")

    def __unicode__(self):
        return "%s for $%d (%s)" % (self.code, self.value,
            "claimed" if self.claimed else "unclaimed")
