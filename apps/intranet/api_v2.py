from rest_framework import viewsets, serializers
from rest_framework.response import Response
from models import Article, Event, Profile, Tournament
from tasks import get_steam_account_for_id

class RendersDefaultTemplate(object):
    template_name = 'index.html'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament


class ArticleViewSet(viewsets.ReadOnlyModelViewSet, RendersDefaultTemplate):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet, RendersDefaultTemplate):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ProfileViewSet(viewsets.ModelViewSet, RendersDefaultTemplate):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request):
        print request.DATA
        try:
            steam_id = request.DATA['steam_id']
            profile = get_steam_account_for_id(steam_id)
            profile.save()
            return Response(ProfileSerializer(profile).data, status=201)
        except KeyError as e:
            return Response(status=400)


class TournamentViewSet(viewsets.ReadOnlyModelViewSet, RendersDefaultTemplate):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
