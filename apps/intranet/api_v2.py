from rest_framework import viewsets, serializers
from models import Entry, Event, Tournament

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

