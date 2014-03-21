from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'users.views.home', name='home'),
    url(r'^sign-up/$', 'users.views.signup', name='signup'),
    url(r'^sign-in/$', 'users.views.signin', name='signin'),
    url(r'^about-us/$', 'users.views.aboutus', name='aboutus'),
    url(r'^language/(P<language>[a-z\-]+)$', 'users.views.language'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #auth
    url(r'^accounts/login/$', 'users.views.login'),
    url(r'^accounts/auth/$', 'users.views.auth_view'),
    url(r'^accounts/logout/$', 'users.views.logout'),
    url(r'^accounts/loggedin/$', 'users.views.loggedin'),
    url(r'^accounts/invalid/$', 'users.views.invalid_login'),
    url(r'^accounts/register/$', 'users.views.register'),
    url(r'^accounts/register_success/$', 'users.views.register_success'),
  
    
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)