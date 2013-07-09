"""Test the auth mixins.
"""
from django.conf import settings
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
