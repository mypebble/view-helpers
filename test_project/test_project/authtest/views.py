from django.http import HttpResponse
from django.views.generic import View

from pebble_helpers.views.mixins import auth


class LoginView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('')


class LoginRequired(auth.LoginRequiredMixin, View):
    """Test the LoginRequiredMixin.
    """


class LoginRequiredRedirect(auth.LoginRequiredMixin, View):
    """Test the LoginRequiredMixin with a redirect_field_name set.
    """
    redirect_field_name = 'go_to'


class NotLoggedIn(View):
    """Test the logged_in_view wrapper with a non-logged in class.
    """
    def get(self, *args, **kwargs):
        """
        """
        return HttpResponse('not logged in class')


class LoggedIn(View):
    """Test the logged_in_view wrapper with a logged-in class.
    """
    def get(self, *args, **kwargs):
        """
        """
        return HttpResponse('logged in class')
