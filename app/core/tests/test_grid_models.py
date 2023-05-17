from django.test import TestCase
from django.utils import timezone
from core.models import Grid


class GridModelTests(TestCase):
    def create_grid(self, points="2,2;-1,30;20,11;4,5", ):
        return Grid.objects.create(points=points, created_at=timezone.now())

    def test_grid_creation(self):
        grid = self.create_grid()
        self.assertTrue(isinstance(grid, Grid))
        self.assertEqual(grid.closest_points, '2,2;4,5')
