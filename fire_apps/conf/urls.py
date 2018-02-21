from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fire_apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(admin.site.urls)),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^vendas/', include('sales.urls', namespace='sales')),
    url(r'^pagamentos/', include('payments.urls', namespace='payments')),
    url(r'^sair/$','django.contrib.auth.views.logout',{'next_page':'login'},name='logout'),
    url(r'^entrar/$','django.contrib.auth.views.login',{'template_name':'payments/login.html'},name='login'),
)

if settings.DEBUG:
	urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))