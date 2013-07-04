"""Mixins for class-based views to assist in managing time.
"""
__author__ = 'Scott Walton <scw@talktopebble.co.uk>'

from datetime import datetime

from dateutil import parser

from django.conf import settings


class CurrentDateTimeMixin(object):
    """Freezes the current datetime to the time at the start of the request.
    Helps with potential issues of a request crossing the day boundary.
    Also adds a TEST_DATETIME request argument that sets the datetime to a
    specific point during the testing environment.
    """
    def dispatch(self, request, *args, **kwargs):
        """Set the datetime for the request.
        """
        self.set_datetime(request)
        return super(
            CurrentDateTimeMixin, self).dispatch(request, *args, **kwargs)

    def set_datetime(self, request):
        """Freezes the datetime of the request. If TESTING is True, also reads
        the request arguments for a TEST_DATETIME that allows us to freeze
        the datetime during a testing environment.
        """
        request_args = getattr(request, request.method, {})
        DATETIME = 'TEST_DATETIME'

        if DATETIME in request_args and settings.TESTING:
            self._datetime = parser.parse(request_args[DATETIME])
        else:
            self._datetime = datetime.now()

    def get_date(self):
        """Get the date of the request starting.
        """
        return self._datetime.date()

    def get_datetime(self):
        """Get the full datetime of the request starting.
        """
        return self._datetime
