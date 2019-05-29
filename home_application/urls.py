# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^api/', include('home_application.api.urls')),
    (r'^register/', include('home_application.register.urls')),
    (r'^goods/', include('home_application.goods.urls')),
)
