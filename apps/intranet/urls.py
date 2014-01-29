from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from api_v2 import ArticleViewSet, EventViewSet, ProfileViewSet, TournamentViewSet
from views import get_steam_account

# V2, rest_framework -- current
router = DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'event', EventViewSet, base_name='event')
router.register(r'profile', ProfileViewSet, base_name='profile')
router.register(r'tournament', TournamentViewSet, base_name='tournament')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^steam-profile/$', get_steam_account, name='steam-ids'),
)
