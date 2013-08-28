from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from core.forms import TopLoginForm, FrontSignUpForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^account/password_reset/', 'django.contrib.auth.views.password_reset', {'html_email_template_name': 'registration/password_reset_html_email.html'}),
    url(r'^account/', include('django.contrib.auth.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'core/index.html',
                                                        'authentication_form': TopLoginForm,
                                                        'extra_context': {'signup_form': FrontSignUpForm()}
                                                        }),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^signup/$', 'core.views.sign_up', name='signup'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^mobile/', include('mobile.urls', namespace='mobile')),
    url(r'^expense/', include('expense.urls', namespace='expense')),
    url(r'^contribute/', include('contribute.urls', namespace='contribute')),
    url(r'^settings/', include('setup.urls', namespace='setup')),
    url(r'^support/', include('support.urls', namespace='support')),
    url(r'^', include('core.urls', namespace='core')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
