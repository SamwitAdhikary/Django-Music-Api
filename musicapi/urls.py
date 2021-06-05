from musicapi.viewsets import SongViewSet, CategoryViewSet, SongCategoryViewSet
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('song', SongViewSet)
router.register('category', CategoryViewSet)
router.register('songcategory', SongCategoryViewSet)

urlpatterns = [
    path("", include(router.urls))
]