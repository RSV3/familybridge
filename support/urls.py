from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  # Examples:
  url(r'^email/render/$', 'support.views.email_render', name='email_render'),
)
