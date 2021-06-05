from musicapi.models import Category, Song
from rest_framework import viewsets
from . import serializer
from django.db.models import Prefetch

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = serializer.Category.objects.all()
    serializer_class = serializer.CategorySerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = serializer.Song.objects.all()
    serializer_class = serializer.SongSerializer

class SongCategoryViewSet(viewsets.ModelViewSet):
    queryset = serializer.Category.objects.all()
    serializer_class = serializer.SongCategorySerializer