from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SongAPITestCase(APITestCase):
    def test_add_song(self):
        """
        Ensure we can add a new song
        """
        url = reverse('training:song-list')
        data = {'title': 'A', 'description': 'Song A', 'notation': 'A1-B2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for k, v in data.items():
            self.assertEqual(response.data[k], v)

    def test_get_song_list(self):
        """
        Ensure we can get song list
        """
        url = reverse('training:song-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WarmUpAPITestCase(APITestCase):
    def test_get_song_list(self):
        """
        Ensure we can get warmup list
        """
        url = reverse('training:warmup-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
