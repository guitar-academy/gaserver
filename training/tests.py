from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from . import factories
from .models import Song, WarmUp

class SongAPITestCase(APITestCase):
    def test_add_song(self):
        """
        Ensure we can add a new song
        """
        n_song = Song.objects.count()
        url = reverse('training:song-list')
        data = {'title': 'A', 'description': 'Song A', 'notation': 'A1-B2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for k, v in data.items():
            self.assertEqual(response.data[k], v)
        self.assertEqual(Song.objects.count(), n_song + 1)

    def test_get_song_list(self):
        """
        Ensure we can get song list
        """
        new_song_count = 13
        total_songs = Song.objects.count() + new_song_count

        song = factories.SongFactory.create_batch(new_song_count)
        url = reverse('training:song-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), total_songs)


class WarmUpAPITestCase(APITestCase):
    def test_get_song_list(self):
        """
        Ensure we can get warmup list
        """

        new_warmup_count = 13
        total_warmup = WarmUp.objects.count() + new_warmup_count
        factories.WarmUpFactory.create_batch(new_warmup_count)
        url = reverse('training:warmup-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), total_warmup)
