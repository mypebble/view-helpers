"""Test the auth mixins.
"""
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class LoginRequiredTestCase(TestCase):
    """Test the LoginRequiredMixin.
    """
    def setUp(self):
        """Set up the test client.
        """
        self.client = Client()

    def test_plain(self):
        """Test the LoginRequiredMixin without overriding the redirect
        paremeter.
        """
        url = reverse('authtest-login')
        response = self.client.get(url)
        redirect_url = '{}?next={}'.format(
            settings.LOGIN_URL, url)
        self.assertRedirects(response, redirect_url)

    def test_redirect_set(self):
        """Test the LoginRequiredMixin by overriding the redirect_field_name
        """
        url = reverse('authtest-redirect')
        response = self.client.get(url)
        redirect_url = '{}?go_to={}'.format(
            settings.LOGIN_URL, url)
        self.assertRedirects(response, redirect_url)


class AlreadyLoggedInTestCase(TestCase):
    """Test the already_logged_in function.
    """
    def setUp(self):
        User.objects.create_user('test_user', 'test@example.com', 'password')

        self.client = Client()
        self.client.login(username='test_user', password='password')

    def test_already_logged_in(self):
        """We send logged in users to the value of next.
        """
        response = self.client.get(
            reverse('logged-in'),
            {'next': reverse('arbitrary-view')})

        self.assertRedirects(response, '/arbitrary_url/')

    def test_already_logged_in_settings_redirect(self):
        """We send logged in users who don't pass in next to the default
        LOGIN_REDIRECT_URL.
        """
        response = self.client.get(reverse('logged-in'))
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)

    def test_not_logged_in(self):
        """We send non-logged in users to the login page.
        """
        self.client.logout()

        response = self.client.get(
            reverse('logged-in'),
            {'next': reverse('arbitrary-view')})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['next'], '/arbitrary_url/')
