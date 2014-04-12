from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
url(r'^$', 'users.views.home', name='home'),
url(r'^signup/$', 'users.views.signup', name='signup'),
url(r'^logout/$', 'users.views.logout', name='logout'),


#auth
url(r'^login/$', 'users.views.login', name='login'),
url(r'^auth/$', 'users.views.auth_view', name='auth_view'),
url(r'^logout/$', 'users.views.logout', name='logout'),


#user
url(r'^userhome/$', 'users.views.user_home', name='user_home'),
url(r'^forms/$', 'users.views.forms', name='forms'),
#url(r'^register/$', 'users.views.register'),
#url(r'^register_success/$', 'users.views.register_success'),


)
