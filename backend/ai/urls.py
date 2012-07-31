from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from apps.intranet.api import *

admin.autodiscover()

api = Api(api_name="v1")
api.register(EntryResource())
api.register(EventResource())
api.register(ServerResource())
api.register(TournamentResource())
api.register(FAQResource())
api.register(BarTabResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls))
)
