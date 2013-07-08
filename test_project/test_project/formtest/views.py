from django.views.generic import View

from pebble_helpers.views.mixins.form import RedirectReverseMixin


class SuccessUrlView(RedirectReverseMixin, View):
    """View that has a Success Url
    """
    success_url = 'testproject-success-plain'


class SuccessUrlArgView(RedirectReverseMixin, View):
    """View that has a Success Url that takes an arg.
    """
    success_url = 'testproject-success-arg'

    def get_success_args(self):
        """
        """
        return 0,


class SuccessUrlKwargView(RedirectReverseMixin, View):
    """View that has a Success Url that takes a kwarg.
    """
    success_url = 'testproject-success-kwarg'

    def get_success_kwargs(self):
        """
        """
        return {'i': 0}


class SuccessUrlArgKwargView(RedirectReverseMixin, View):
    """View that has both get_success_kwargs and get_success_args defined.
    """
    success_url = 'testproject-success-argkwarg'

    def get_success_args(self):
        """
        """
        return 0,

    def get_success_kwargs(self):
        """
        """
        return {'i': 0}


class FailureUrlView(RedirectReverseMixin, View):
    """View that has a Failure Url
    """
    failure_url = 'testproject-failure-plain'


class FailureUrlArgView(RedirectReverseMixin, View):
    """View that has a Failure Url that takes an Arg.
    """
    failure_url = 'testproject-failure-arg'

    def get_failure_args(self):
        """
        """
        return 0,


class FailureUrlKwargView(RedirectReverseMixin, View):
    """View that has a Failure Url that takes a kwarg.
    """
    failure_url = 'testproject-failure-kwarg'

    def get_failure_kwargs(self):
        """
        """
        return {'i': 0}


class FailureUrlArgKwargView(RedirectReverseMixin, View):
    """View that has both get_failure_kwargs and get_failure_args defined.
    """
    failure_url = 'testproject-failure-argkwarg'

    def get_failure_args(self):
        """
        """
        return 0,

    def get_failure_kwargs(self):
        """
        """
        return {'i': 0}


class NoUrlView(RedirectReverseMixin, View):
    """View that has neither a Success or Failure Url.
    """
