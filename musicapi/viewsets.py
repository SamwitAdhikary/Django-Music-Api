from rest_framework import viewsets
from . import serializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = serializer.Category.objects.all()
    serializer_class = serializer.CategorySerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = serializer.Song.objects.all()
    serializer_class = serializer.SongSerializer