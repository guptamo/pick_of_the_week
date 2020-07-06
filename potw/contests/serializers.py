from rest_framework import serializers
from .models import Contest, Pick

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'

class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = '__all__'
