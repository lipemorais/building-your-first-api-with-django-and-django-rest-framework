from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ArtistViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index'),
]
