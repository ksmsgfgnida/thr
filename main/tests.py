from django.test import TestCase
from django.contrib.auth.models import User, Group

class UserRoleTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='adminpass')
        admin_group = Group.objects.create(name='Administrator')
        self.admin_user.groups.add(admin_group)

        self.user = User.objects.create_user(username='user', password='userpass')
        user_group = Group.objects.create(name='User')
        self.user.groups.add(user_group)

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.guest_client = Client()

    def test_admin_access(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_user_access(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 403)

    def test_guest_access_to_order_page(self):
        response = self.guest_client.get('/profile/')
        self.assertEqual(response.status_code, 403)

