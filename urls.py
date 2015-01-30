from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^admin/', include(admin.site.urls)),
    (r'^account/',include('account.urls')),

    #url(r'^aboutus',direct_to_template, {'template':'static/aboutus.html'},name='aboutus'),
    url(r'^contactus',direct_to_template, {'template':'bootstrap/static/contactus.html'},name='contactus'),
	 url(r'^accrediation',direct_to_template, {'template':'bootstrap/static/Accrediation.html'},name='accrediation'),
    #url(r'^categories',direct_to_template, {'template':'website/categories.html'}),
    url(r'^underConstruction',direct_to_template, {'template':'static/underConstruction.html'}),
    
    (r'^', include('website.urls')),
)

urlpatterns += patterns("django.views",
        url(r'^media(?P<path>.*)/$',
            "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )
