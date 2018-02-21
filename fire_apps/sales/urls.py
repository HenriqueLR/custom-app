from django.conf.urls import patterns, include, url

urlpatterns = patterns('sales.views',

    url(r'^novo_cliente/$', 'add_customer', name='add_customer'),
    url(r'^clientes/$', 'list_customer', name='list_customer'),
)