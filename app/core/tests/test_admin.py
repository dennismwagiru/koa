from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import Grid


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@koa.co.ke',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@koa.co.ke',
            password='password123',
            name='Test user full name'
        )
        self.grid = Grid.objects.create(points='2,2;-1,30;20,11;4,5')

    def test_for_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_for_grids_listed(self):
        """Test that grids are listed on the grids page"""
        url = reverse('admin:core_grid_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.grid.points)
        self.assertContains(res, self.grid.closest_points)

    def test_grid_change_page(self):
        """Test that the grid edit page works"""
        url = reverse('admin:core_grid_change', args=[self.grid.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_grid_page(self):
        """Test that the create grid page works"""
        url = reverse('admin:core_grid_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
