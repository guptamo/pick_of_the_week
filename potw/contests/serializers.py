from rest_framework import serializers
from .models import Contest, Pick


class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = '__all__'


class ContestSerializer(serializers.ModelSerializer):
    pick_set = PickSerializer(many=True, read_only=True)
    status = serializers.CharField(source='get_status', read_only=True)

    class Meta:
        model = Contest
        fields = ['theme',
                   'pick_deadline',
                   'vote_deadline',
                   'admin_id',
                   'spotify_playlist',
                   'youtube_playlist',
                   'pick_set',
                   'status']
