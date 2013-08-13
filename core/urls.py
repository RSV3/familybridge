from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.index', name='index'),
    url(r'^home/$', 'core.views.home', name='home'),
    url(r'^profile/$', 'core.views.profile', name='profile'),
    url(r'^about/$', 'core.views.about', name='about'),
)
