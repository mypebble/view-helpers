from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect, resolve_url
from django.utils.http import is_safe_url

from django.contrib.auth.decorators import login_required


def already_logged_in(login_function):
    """Wraps login_function with a redirect to the desired URL if the user is
    already logged in.
    NOTE: login_function must be the function you wish to call. This wrapper
    does not work with the string format accepted by Django's URL syntax.
    """
    def check_login(request, *args, **kwargs):
        """Checks whether the user is logged in or not. If they are, redirects
        to the "next" parameter, otherwise displays the login_function.
        """
        if request.method == 'GET' and request.user.is_authenticated():
            redirect_field_name = kwargs.get(
                'redirect_field_name', REDIRECT_FIELD_NAME)

            redirect_to = request.REQUEST.get(
                redirect_field_name, settings.LOGIN_REDIRECT_URL)

            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            rtn = redirect(redirect_to)
        else:
            rtn = login_function(request, *args, **kwargs)

        return rtn

    return check_login


class LoginRequiredMixin(object):
    """Applies the login_required decorator to the as_view class method of a
    view.
    Simply inherit from this class to get the benefits.
    """
    redirect_field_name = 'next'

    @classmethod
    def as_view(cls, **initkwargs):
        """
        """
        view = super(LoginRequiredMixin, cls).as_view
        return login_required(
                view(**initkwargs),
                redirect_field_name=cls.redirect_field_name)
