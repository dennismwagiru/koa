from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Grid

GRID_URL = reverse('core:grid-list')


class GridApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_grid_empty_points(self):
        """Test creating a new grid with an empty payload"""
        payload = {'points': ''}
        res = self.client.post(GRID_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_grid_invalid(self):
        """Test creating a new grid with an invalid payload"""
        payload = {'points': '2,2;7;9'}
        res = self.client.post(GRID_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_grid_successful(self):
        """Test creating a new grid"""
        payload = {'points': '2,2;-1,30;20,11;4,5'}
        res = self.client.post(GRID_URL, payload)

        exists = Grid.objects.filter(
            points=payload['points'],
            closest_points='2,2;4,5'
        ).exists()
        self.assertTrue(exists)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
