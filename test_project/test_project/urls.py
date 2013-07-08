from django.conf.urls.defaults import url, patterns


from test_project.formtest.views import (FailureUrlView, FailureUrlArgView,
        SuccessUrlView, SuccessUrlArgView)


urlpatterns = patterns('',
    url('/success/plain/',
        SuccessUrlView.as_view(),
        name='testproject-success-plain'),
    url('/success/args/(?P<i>\d+',
        SuccessUrlArgView.as_view(),
        name='testproject-success-arg'),

    url('/failure/plain/',
        FailureUrlView.as_view(),
        name='testproject-failure-plain'),
    url('/failure/args/(?P<i>\d+',
        FailureUrlArgView.as_view(),
        name='testproject-failure-arg'),
)
