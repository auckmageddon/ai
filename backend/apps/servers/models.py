from django.db import models

class Server(models.Model):
    address     = models.CharField(max_length=21, unique=False)
    game        = models.CharField(max_length=100)
    name        = models.CharField(max_length=200)
    players     = models.IntegerField()
    max_players = models.IntegerField()
    map         = models.CharField(max_length=50)
    last_seen   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s at %s" % (self.game, self.address)