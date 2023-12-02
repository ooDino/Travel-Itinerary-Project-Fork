from django.test import TestCase
from django.urls import reverse

class LoginUnitTest(TestCase):

    def test_login_view_rejects_empty_username(self):
        response = self.client.post(reverse('login'), {'username': '', 'password': 'password'})
        self.assertFormError(response, 'form', 'username', 'This field is required.')

    def test_login_view_rejects_empty_password(self):
        response = self.client.post(reverse('login'), {'username': 'user', 'password': ''})
        self.assertFormError(response, 'form', 'password', 'This field is required.')
