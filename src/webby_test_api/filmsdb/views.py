from rest_framework import viewsets
from rest_framework.response import Response
from filmsdb.models import Film, Actor
from filmsdb.serializers import FilmSerializer


class FilmViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Film.objects.all()
        serializer = FilmSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Film.objects.all()
        work = get_object_or_404(queryset, pk=pk)
        serializer = FilmSerializer(queryset, context={'request': request})
        return Response(serializer.data)
