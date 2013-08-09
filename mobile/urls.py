from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mobile.views.index', name='index'),
)
