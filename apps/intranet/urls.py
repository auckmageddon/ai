from django.conf.urls import patterns, include, url
from tastypie.api import Api
from rest_framework.routers import DefaultRouter
from api_v1 import EntryResource, EventResource, TournamentResource
from api_v2 import EntryViewSet, EventViewSet, TournamentViewSet

# V1, tastypie -- deprecated
api = Api(api_name='v1')
api.register(EntryResource())
api.register(EventResource())
api.register(TournamentResource())

# V2, rest_framework -- current
router = DefaultRouter()
router.register(r'entry', EntryViewSet)
router.register(r'event', EventViewSet)
router.register(r'tournament', TournamentViewSet)

urlpatterns = patterns('',
    url(r'^v2/', include(router.urls)),
    url(r'', include(api.urls)),
)
