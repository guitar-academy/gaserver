from rest_framework import serializers
from .models import Song, Skill, WarmUp


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill

class WarmUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarmUp
