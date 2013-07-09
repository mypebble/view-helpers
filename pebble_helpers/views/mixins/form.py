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


class FormRedirectMixin(object):
    """Checks for redirect_field_name in the submitted request. The value of
    this is used to redirect the user to another page upon validating the form.
    If the redirect field is not set, then this mixin falls back to the view's
    default behaviour.

    This mixin is currently incompatible with RedirectReverseMixin.
    """
    redirect_field_name = 'next'

    def form_valid(self, form):
        method_dict = getattr(self.request, self.request.method)
        next_url = method_dict.get(self.redirect_field_name)
        if next_url is None and self.request.method != 'GET':
            next_url = self.request.GET.get(self.redirect_field_name)

        if next_url is not None:
            self.success_url = next_url

        return super(FormRedirectMixin, self).form_valid(form)
