from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.index', name='index'),
    url(r'^home/$', 'core.views.home', name='home'),
    url(r'^profile/$', 'core.views.profile', name='profile'),
    url(r'^about/$', 'core.views.about', name='about'),
    url(r'^invite/team/members/$', 'core.views.invite_team_members', name='invite_team_members'),
    url(r'^mark/paid/(?P<payment_id>\d+)/$', 'core.views.mark_paid', name='mark_paid'),
    url(r'^payments/$', 'core.views.payments', name='payments'),
    url(r'^expense/add/$', 'core.views.add_expense', name='add_expense'),
    url(r'^change/group/name/(?P<group_id>\d+)/$', 'core.views.change_group_name', name='change_group_name'),
)
