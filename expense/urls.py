from django.conf.urls import patterns, url

urlpatterns = patterns('',
  # Examples:
  url(r'^$', 'expense.views.index', name='index'),
  url(r'^add/$', 'expense.views.add_expense', name='add_expense'),
  url(r'^contributor/mixin/add/$', 'expense.views.add_contributor_mixin', name='add_contributor_mixin'),
  url(r'^contributions/$', 'expense.views.contributions', name='contributions'),
  url(r'^requested/contributions/$', 'expense.views.requested_contributions', name='requested_contributions'),
  url(r'^teammembers/add/$', 'expense.views.add_teammembers', name='add_teammembers'),
  url(r'^teammember/mixin/add/$', 'expense.views.add_teammember_mixin', name='add_teammember_mixin'),
  url(r'^bankcard/add/$', 'expense.views.add_bank_card', name='add_bank_card'),
  url(r'^multiple/add/$', 'expense.views.add_multiple_expenses', name='add_multiple_expenses'),
  url(r'^contribute/(?P<contribution_id>\d+)/$', 'expense.views.contribute_to_contribution', name='contribute_to_contribution'),
  url(r'^decline/(?P<contribution_id>\d+)/$', 'expense.views.decline_contribution', name='decline_contribution'),
)
