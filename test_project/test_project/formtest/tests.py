"""
Test the Form-based view mixins.
"""

from django.test import TestCase

from test_project.formtest.views import (FailureUrlView, FailureUrlArgView,
        FailureUrlKwargView, FailureUrlArgKwargView, SuccessUrlView,
        SuccessUrlArgView, SuccessUrlKwargView, SuccessUrlArgKwargView,
        NoUrlView)


class RedirectReverseTestCase(TestCase):
    """Test the RedirectReverseTestCase.
    """
    def test_success_url_plain(self):
        """Test the success url is reversed.
        """
        v = SuccessUrlView()
        self.assertEqual(v.get_success_url(), '/success/plain/')

    def test_failure_url_plain(self):
        """Test the failure url is reversed.
        """
        v = FailureUrlView()
        self.assertEqual(v.get_failure_url(), '/failure/plain/')

    def test_success_url_arg(self):
        """Test the success url is reversed with the given arg.
        """
        v = SuccessUrlArgView()
        self.assertEqual(v.get_success_url(), '/success/arg/0/')

    def test_failure_url_arg(self):
        """Test the failure url is reversed with the given arg.
        """
        v = FailureUrlArgView()
        self.assertEqual(v.get_failure_url(), '/failure/arg/0/')

    def test_success_url_kwarg(self):
        """Test the success url is reversed with the given kwarg.
        """
        v = SuccessUrlKwargView()
        self.assertEqual(v.get_success_url(), '/success/kwarg/0/')

    def test_failure_url_kwarg(self):
        """Test the failure url is reversed with the given kwarg.
        """
        v = FailureUrlKwargView()
        self.assertEqual(v.get_failure_url(), '/failure/kwarg/0/')

    def test_success_argkwarg(self):
        """We get a ValueError on defining both args and kwargs.
        """
        v = SuccessUrlArgKwargView()

        self.assertRaises(ValueError, v.get_success_url)

    def test_failure_argkwarg(self):
        """We get a ValueError on defining both args and kwargs.
        """
        v = FailureUrlArgKwargView()

        self.assertRaises(ValueError, v.get_failure_url)

    def test_no_success_url(self):
        """We get an error when no success_url is defined.
        """
        v = NoUrlView()
        self.assertRaises(NotImplementedError, v.get_success_url)

    def test_no_failure_url(self):
        """We get an error when no failure_url is defined.
        """
        v = NoUrlView()
        self.assertRaises(NotImplementedError, v.get_failure_url)
