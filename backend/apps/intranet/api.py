from tastypie.resources import ModelResource
from models import Entry, Event, Server, Tournament, FAQ, BarTab


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'


class ServerResource(ModelResource):
    class Meta:
        queryset = Server.objects.all()
        resource_name = 'server'


class FAQResource(ModelResource):
    class Meta:
        queryset = FAQ.objects.all()
        resource_name = 'faq'


class TournamentResource(ModelResource):
    class Meta:
        queryset = Tournament.objects.all()
        resource_name = 'tournament'


class BarTabResource(ModelResource):
    class Meta:
        queryset = BarTab.objects.all()
        resource_name = 'bartab'
