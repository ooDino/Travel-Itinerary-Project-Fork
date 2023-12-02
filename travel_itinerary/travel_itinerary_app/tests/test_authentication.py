from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationIntegrationTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testing',
            'password': 'RightPassword'
        }
        User.objects.create_user(**self.credentials)

    def test_successful_login(self):
        response = self.client.post(reverse('login'), self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_successful_logout(self):
        self.client.post(reverse('login'), self.credentials, follow=True)   
        response = self.client.get(reverse('logout'), follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_login_with_wrong_credentials(self):
        wrong_credentials = {
            'username': 'testing',
            'password': 'WrongPassword'
        }
        response = self.client.post(reverse('login'), wrong_credentials, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
