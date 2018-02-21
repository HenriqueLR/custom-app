from django.conf.urls import patterns, include, url

urlpatterns = patterns('catalog.views',
	
	url(r'^$', 'list_catalog', name='list_catalog'),
)