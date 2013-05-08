from django.contrib import admin
admin.autodiscover()
from django.conf.urls.defaults import *
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView

import registration.backends.default.urls as regUrls

from profile import UserRegistrationForm
from registration.views import register
import regbackend, views

urlpatterns = patterns('', 
	url(r'^admin/', include(admin.site.urls)),	
	# (r'^conf/admin/(.*)', admin.site.root),
	url(r'^accounts/register/$', register, {'backend': 'registration.backends.default.DefaultBackend','form_class': UserRegistrationForm}, name='registration_register'),
	(r'^accounts/', include(regUrls)),
	url(r'^go/profile/$', 
                           TemplateView.as_view(template_name="profile.html"),
                           'profile'),
	# url('^go/profile/$', direct_to_template, {'template': 'profile.html'}, name="profile"),
	(r'^$', views.index),	
)
