from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from core.models import Grid


def sample_user(email='test@koa.co.ke', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class UserModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        password = 'testpass'
        user = sample_user(password=password)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@KOA.CO.KE'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@koa.co.ke',
            'test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


class GridModelTests(TestCase):
    def create_grid(self, points="2,2;-1,30;20,11;4,5", ):
        return Grid.objects.create(points=points, created_at=timezone.now())

    def test_grid_creation(self):
        grid = self.create_grid()
        self.assertTrue(isinstance(grid, Grid))
        self.assertEqual(grid.closest_points, '2,2;4,5')
