from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'expense.views.index', name='index'),
    url(r'^add/$', 'expense.views.add_expense', name='add_expense'),
    url(r'^contributions/$', 'expense.views.contributions', name='contributions'),
    url(r'^contributors/add/$', 'expense.views.add_contributors', name='add_contributors'),
    url(r'^bankcard/add/$', 'expense.views.add_bank_card', name='add_bank_card'),
    url(r'^multiple/add/$', 'expense.views.add_multiple_expenses', name='add_multiple_expenses'),
)
