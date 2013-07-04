"""Test the time helpers
"""
from datetime import date, datetime

from django.http import HttpRequest, QueryDict
from django.test import TestCase

from pebble_helpers.views.mixins import time


class CurrentDateTimeTestCase(TestCase):
    """Test the CurrentDateTimeMixin.
    """

    def setUp(self):
        """Create the HTTP Request and data.
        """
        CURRENT_DATETIME = '2013-07-14T13:01:14.034159'

        query_arg = u'TEST_DATETIME={0}'.format(CURRENT_DATETIME)

        self.query = QueryDict(query_arg)
        self.request = HttpRequest()

    def test_set_datetime_get(self):
        """Set the datetime in a request GET.
        """
        self.request.method = 'GET'
        self.request.GET = self.query

        datetime_mixin = time.CurrentDateTimeMixin()
        datetime_mixin.set_datetime(self.request)

        dtime = datetime(2013, 7, 14, 13, 1, 14, 34159)
        dt = date(2013, 7, 14)

        self.assertEqual(datetime_mixin.get_date(), dt)
        self.assertEqual(datetime_mixin.get_datetime(), dtime)

    def test_set_datetime_post(self):
        self.request.method = 'POST'
        self.request.POST = self.query

        datetime_mixin = time.CurrentDateTimeMixin()
        datetime_mixin.set_datetime(self.request)

        dtime = datetime(2013, 7, 14, 13, 1, 14, 34159)
        dt = date(2013, 7, 14)

        self.assertEqual(datetime_mixin.get_date(), dt)
        self.assertEqual(datetime_mixin.get_datetime(), dtime)
