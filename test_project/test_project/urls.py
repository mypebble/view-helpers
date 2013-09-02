from django.conf.urls.defaults import url, patterns
from django.contrib.auth.views import login


from pebble_helpers.views.mixins.auth import already_logged_in

from test_project.formtest.views import (FailureUrlView, FailureUrlArgView,
        FailureUrlKwargView, FailureUrlArgKwargView, SuccessUrlView,
        SuccessUrlArgView, SuccessUrlKwargView, SuccessUrlArgKwargView)

from test_project.authtest.views import (LoginRequired, LoginRequiredRedirect,
        LoginView)


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

urlpatterns += patterns('',
    url(r'login/$',
        LoginView.as_view(),
        name='login'),
    url(r'^auth/plain/$',
        LoginRequired.as_view(),
        name='authtest-login'),
    url(r'^auth/redirect/$',
        LoginRequiredRedirect.as_view(),
        name='authtest-redirect'),
)

urlpatterns += patterns('',
    url(r'^already_logged_in/$',
        already_logged_in(login),
        name='logged-in'),
    url(r'^arbitrary_url/$',
        LoginView.as_view(),
        name='arbitrary-view'),
    url(r'^settings_defined/$',
        LoginView.as_view(),
        name='settings-defined'),
)
