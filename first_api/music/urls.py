from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ArtistViewSet, AlbumViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index'),
]
