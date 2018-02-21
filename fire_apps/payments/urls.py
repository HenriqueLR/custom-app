#coding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('payments.views',
    url(r'^$', 'dash_payments', name='dash_payments'),
    url(r'^lancamentos/$', 'list_lancamentos', name='list_lancamentos'),
    url(r'^novo_lancamento/$', 'add_lancamentos', name='add_lancamentos'),
    url(r'^apagar_lancamento/(?P<pk>\d+)$', 'delete_credit_debit', name='delete_credit_debit'),
    url(r'^detalhar_lancamento/(?P<pk>\d+)$', 'detail_credit_debit', name='detail_credit_debit'),
    url(r'^verify_payments/$', 'check_payments', name='check_payments'),
)
