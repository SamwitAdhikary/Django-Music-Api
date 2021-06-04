from rest_framework import serializers
from .models import Song, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    song_category = CategorySerializer()
    class Meta:
        model = Song
        fields = '__all__'