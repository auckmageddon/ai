from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from apps.intranet.api_v1 import EntryResource, EventResource, TournamentResource
from apps.intranet.views import IndexView

admin.autodiscover()

api = Api(api_name="v1")
api.register(EntryResource())
api.register(EventResource())
api.register(TournamentResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
    url(r'^$', IndexView.as_view()),
    # url(r'^screen\.html$', 'django.views.generic.simple.direct_to_template', {'template': 'screen.html'})
)
