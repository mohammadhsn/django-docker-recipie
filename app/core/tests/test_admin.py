from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        self.admin = get_user_model().objects.create_superuser(
            email='admin@django.com',
            password='123456789'
        )

        self.client.force_login(self.admin)
        self.user = get_user_model().objects.create_user(
            email='mohammad@gmail.com',
            password='12345678',
            name='Test user'
        )

    def test_users_listed(self):
        response = self.client.get(reverse('admin:core_user_changelist'))
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        response = self.client.get(
            reverse('admin:core_user_change', args=(self.user.id,))
        )

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        response = self.client.get(reverse('admin:core_user_add'))
        self.assertEqual(response.status_code, 200)
