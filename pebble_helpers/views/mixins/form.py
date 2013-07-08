"""Helpers for views that deal with CRUD operations.
"""
from django.core.urlresolvers import reverse


class RedirectReverseMixin(object):
    """Calls reverse on success/failure URLs passed into the class.
    """
    def get_success_url(self):
        """Returns the success URL after reversing the url name passed.
        """
        success_url = getattr(self, 'success_url', None)
        if success_url is None:
            raise NotImplementedError(
                u'You must defined a success_url on this class')

        return reverse(
            self.success_url, args=self.get_success_args(),
            kwargs=self.get_success_kwargs())

    def get_failure_url(self):
        """Returns the failure URL after reversing the url name passed.
        """
        failure_url = getattr(self, 'failure_url', None)
        if failure_url is None:
            raise NotImplementedError(
                u'You must defined a failure_url on this class')

        return reverse(
            self.failure_url, args=self.get_failure_args(),
            kwargs=self.get_failure_kwargs())

    def get_success_args(self):
        """Override this to return args for the reverse call for success_url
        """
        return ()

    def get_success_kwargs(self):
        """Override this to return kwargs for the reverse call for success_url
        """
        return {}

    def get_failure_args(self):
        """Override this to return args for the reverse call for failure_url
        """
        return ()

    def get_failure_kwargs(self):
        """Override this to return kwargs for the reverse call for failure_url
        """
        return {}
