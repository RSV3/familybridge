from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from core.forms import TopLoginForm, FrontSignUpForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'core/index.html',
                                                        'authentication_form': TopLoginForm,
                                                        'extra_context': {'signup_form': FrontSignUpForm()}
                                                        }),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^signup/$', 'core.views.sign_up', name='signup'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^mobile/', include('mobile.urls', namespace='mobile')),
    url(r'^', include('core.urls', namespace='core')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
