from rest_framework import serializers
from .models import videos,chunk

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=videos
        fields='__all__'

class ChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model=chunk
        fields='__all__'

