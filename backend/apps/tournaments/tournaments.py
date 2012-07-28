from tastypie.resources import ModelResource
from tournaments.models import Tournament

class TournamentResource(ModelResource):
    class Meta:
        queryset = Tournament.objects.all()
        resource_name = 'tournament'
