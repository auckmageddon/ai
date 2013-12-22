from tastypie.resources import ModelResource
from models import Entry, Event, Tournament
import datetime


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.filter(is_published=True)[0:6]
        resource_name = 'entry'


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'


class TournamentResource(ModelResource):
    class Meta:
        queryset = Tournament.objects.all()
        resource_name = 'tournament'
