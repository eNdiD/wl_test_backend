from rest_framework import viewsets, mixins
from rest_framework.response import Response
from filmsdb.models import Film, Actor
from filmsdb.serializers import FilmSerializer, ActorSerializer


class FilmViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class ActorViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
