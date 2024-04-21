from rest_framework import serializers

from music.models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']
