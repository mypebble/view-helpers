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
                u'You must define a success_url on this class')

        return reverse(self.success_url, **self._get_reverse_kwargs('success'))

    def get_failure_url(self):
        """Returns the failure URL after reversing the url name passed.
        """
        failure_url = getattr(self, 'failure_url', None)
        if failure_url is None:
            raise NotImplementedError(
                u'You must define a failure_url on this class')

        return reverse(
            self.failure_url, **self._get_reverse_kwargs('failure'))

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

    def _get_reverse_kwargs(self, direction='success'):
        """Gets the args or kwargs to pass into reverse.
        """
        reverse_kwargs = {}
        if direction == 'success':
            args = self.get_success_args()
            kwargs = self.get_success_kwargs()

        elif direction == 'failure':
            args = self.get_failure_args()
            kwargs = self.get_failure_kwargs()

        if args and kwargs:
            _msg = (
                u"You must only define one of get_{0}_args or "
                u"get_{0}_kwargs".format(direction))
            raise ValueError(_msg)

        if args:
            reverse_kwargs['args'] = args
        elif kwargs:
            reverse_kwargs['kwargs'] = kwargs

        return reverse_kwargs
