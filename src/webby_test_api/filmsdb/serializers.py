from rest_framework import serializers
from filmsdb.models import Film, Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('pk', 'name',)


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('pk', 'title', 'year', 'format', 'actors')
