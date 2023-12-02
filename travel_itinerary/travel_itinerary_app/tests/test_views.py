from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from travel_itinerary_app.forms import SignupForm, LoginForm

class ViewTestCase(TestCase):
    def setUp(self):
        # Set up data for the tests
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'Testpassword123',
        }
        self.user = User.objects.create_user(
            username=self.user_data['username'], 
            email=self.user_data['email'], 
            password=self.user_data['password']
        )

        # URLs for views
        self.home_url = reverse('home')
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.itinerary_url = reverse('itinerary')
        self.profile_url = reverse('profile')
        self.itinerary_form_url = reverse('itinerary_form')
        self.search_results_url = reverse('search_results')

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'travel_itinerary_app/home.html')

    def test_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], SignupForm)

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_itinerary_view(self):
        self.client.login(username='testuser', password='Testpassword123')
        response = self.client.get(self.itinerary_url)
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='testuser', password='Testpassword123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)


    def test_search_results_view_post(self):
        post_data = {
            'business': 'test_business',
            'Destination City': 'test_city'
        }
        response = self.client.post(self.search_results_url, post_data)
        self.assertEqual(response.status_code, 200)
 