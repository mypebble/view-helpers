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
