from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, default='')
    category_image = models.ImageField(upload_to='category_image', blank=True)

    def __str__(self):
        return self.category

class Song(models.Model):
    song_name = models.CharField(max_length=50, default='')
    singer_name = models.CharField(max_length=50, default='')
    song_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    upload_song = models.FileField(upload_to='songs', blank=True)
    song_image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.song_name
