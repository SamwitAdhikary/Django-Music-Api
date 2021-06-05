from rest_framework import serializers
from .models import Song, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    # song_category = CategorySerializer()
    class Meta:
        model = Song
        fields = '__all__'

class SongCategorySerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField('getsongs')

    def getsongs(self, category):
        qs = Song.objects.filter(song_category=category)
        serializer = SongSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = '__all__'