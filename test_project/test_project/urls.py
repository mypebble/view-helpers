from django.conf.urls.defaults import url, patterns


from test_project.formtest.views import (FailureUrlView, FailureUrlArgView,
        FailureUrlKwargView, FailureUrlArgKwargView, SuccessUrlView,
        SuccessUrlArgView, SuccessUrlKwargView, SuccessUrlArgKwargView)


urlpatterns = patterns('',
    url(r'^success/plain/$',
        SuccessUrlView.as_view(),
        name='testproject-success-plain'),
    url(r'^success/arg/(?P<i>\d+)/$',
        SuccessUrlArgView.as_view(),
        name='testproject-success-arg'),
    url(r'^success/kwarg/(?P<i>\d+)/$',
        SuccessUrlKwargView.as_view(),
        name='testproject-success-kwarg'),
    url(r'^success/argkwarg/(?P<i>\d+)/$',
        SuccessUrlArgKwargView.as_view(),
        name='testproject-success-argkwarg'),

    url(r'^failure/plain/$',
        FailureUrlView.as_view(),
        name='testproject-failure-plain'),
    url(r'^failure/arg/(?P<i>\d+)/$',
        FailureUrlArgView.as_view(),
        name='testproject-failure-arg'),
    url(r'^failure/kwarg/(?P<i>\d+)/$',
        FailureUrlKwargView.as_view(),
        name='testproject-failure-kwarg'),
    url(r'^failure/argkwarg/(?P<i>\d+)/$',
        FailureUrlArgKwargView.as_view(),
        name='testproject-failure-argkwarg'),
)
