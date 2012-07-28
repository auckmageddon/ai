from tastypie.resources import ModelResource
from servers.models import Server

class ServerResource(ModelResource):
    class Meta:
        queryset = Server.objects.all()
        resource_name = 'server'
