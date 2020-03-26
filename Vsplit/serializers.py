from rest_framework import serializers
from .models import videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=videos
        fields='_all_'

class ChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model=videos
        fields='_all_'
        
