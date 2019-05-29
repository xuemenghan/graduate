# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.api.views',
    (r'^get_apps/$', 'get_apps'),
    (r'^get_set/$', 'get_set'),
    (r'^get_hosts/$', 'get_hosts'),
    (r'^search_module/$', 'search_module'),
    (r'^fast_script/$', 'fast_script'),
    (r'^inp/$', 'inp'),
    (r'^get_record/$', 'get_record'),
    (r'^loop/$', 'loop'),
    (r'^change/$', 'change'),
    (r'^search/$', 'search'),
    (r'^get_detail/$', 'get_detail'),
)
