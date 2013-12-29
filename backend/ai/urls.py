from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.intranet.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('apps.intranet.urls')),
    url(r'^$', IndexView.as_view()),
    # url(r'^screen\.html$', 'django.views.generic.simple.direct_to_template', {'template': 'screen.html'})
)
