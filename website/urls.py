from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
urlpatterns = patterns('',
#    (r'^articles/2003/$', 'news.views.special_case_2003'),
#    (r'^articles/(\d{4})/$', 'news.views.year_archive'),
#    (r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),
#    (r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),

    url(r'^$',direct_to_template, {'template':'bootstrap/landing/index.html'},name='index'),
     (r'^categories/$','website.views.show_category'),
     url(r'^aboutus/$','website.views.show_aboutus' ,name='aboutus'),
     (r'^(?P<catname>[-\w]*)/(?P<subcatname>[-\w]*)/(?P<catid>\d+)/(?P<subcatid>\d+)/$','website.views.show_product'),
     (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
	 (r'^sitemap\.xml$', direct_to_template, {'template': 'sitemap.xml', 'mimetype': 'text/xml'}),
     (r'^management/$','website.views.management'),
)