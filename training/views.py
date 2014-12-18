from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny


from .models import Song, Skill, WarmUp, SongSkill, WarmUpSong
from .serializers import (
        SongSerializer, SkillSerializer, WarmUpSerializer,
        SongSkillSerializer, WarmUpSongSerializer)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class WarmUpViewSet(viewsets.ModelViewSet):
    queryset = WarmUp.objects.all()
    serializer_class = WarmUpSerializer

class SongSkillViewSet(viewsets.ModelViewSet):
    queryset = SongSkill.objects.all()
    serializer_class = SongSkillSerializer

class WarmUpSongViewSet(viewsets.ModelViewSet):
    queryset = WarmUpSong.objects.all()
    serializer_class = WarmUpSongSerializer


@api_view(('GET',))
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({
        'songs': reverse('training:song-list', request=request,
            format=format),
        'skills': reverse('training:skill-list', request=request,
            format=format),
        'warmups': reverse('training:warmup-list', request=request,
            format=format),
        'songs-skills': reverse('training:songskill-list', request=request,
            format=format),
        'warmups-songs': reverse('training:warmupsong-list', request=request,
            format=format),
    })

