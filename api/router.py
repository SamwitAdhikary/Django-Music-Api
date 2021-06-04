from musicapi.viewsets import SongViewSet, CategoryViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('song', SongViewSet)
router.register('category', CategoryViewSet)