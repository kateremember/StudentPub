from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webadmin.views.home', name='home'),
    # url(r'^webadmin/', include('webadmin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    	url(r'^grappelli/', include('grappelli.urls')),
    	url(r'^admin/', include(admin.site.urls)),
    	#user login, default set the accounts login 
	url(r'^accounts/login/$', 'engine.account.userlogin', name="userlogin"),
    	# user import the url anywhere
	url(r'^$', 'engine.views.index'),

)
