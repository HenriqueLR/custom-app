#coding: utf-8

from django.contrib import admin
from payments.models import (StatusCreditDebit, MachineCard, TipoCreditDebit, Feriados,
                             TaxaMachineCard, SalesCreditDebit, DetailSalesCreditDebit)



class DefaultFields(admin.ModelAdmin):

    def criado(self, obj):
        return obj.created_at.strftime('%d/%m/%Y %H:%M:%S')

    def atualizado(self, obj):
        return obj.updated_at.strftime('%d/%m/%Y %H:%M:%S')



class FeriadosAdmin(DefaultFields):
    list_display = ('name', 'dia', 'mes', 'ano')
    search_fields = ('name','dia', 'mes', 'ano')



class StatusCreditDebitAdmin(DefaultFields):
    list_display = ('name', 'description')
    search_fields = ('name',)



class MachineCardAdmin(DefaultFields):
    list_display = ('name', 'description')
    search_fields = ('name',)



class TaxaMachineCardCardAdmin(DefaultFields):
    list_display = ('machinecard', 'count_parc', 'taxa', 'tipo')
    search_fields = ('machine_card__machinecard', 'count_parc', 'taxa', 'TipoCreditDebit__tipo')
    list_filter = ('tipo', 'machinecard',)



class TipoCreditDebitAdmin(DefaultFields):
    list_display = ('name', 'description')
    search_fields = ('name',)



class SalesCreditDebitAdmin(DefaultFields):
    list_display = ('status', 'tipo', 'cod_venda', 'machinecard', 'total_parc',
                    'valor_total', 'valor_calc', 'valor_perdido_total')
    search_fields = ('status_credit_debit__status', 'tipo_credit_debit__tipo', 'machine__card__machinecard')
    list_filter = ('status', 'tipo', 'machinecard')



class DetailSalesCreditDebitAdmin(DefaultFields):
    list_display = ('sale_credit_debit', 'current_parc', 'valor_parcela',
                    'valor_perdido_parc', 'data_process', 'status_detail')
    search_fields = ('sales_credit_debit__sale_credit_debit','current_parc', 'valor_total', 'valor_calc',
                    'valor_parcela', 'valor_perdido')



admin.site.register(StatusCreditDebit, StatusCreditDebitAdmin)
admin.site.register(MachineCard, MachineCardAdmin)
admin.site.register(TipoCreditDebit, TipoCreditDebitAdmin)
admin.site.register(SalesCreditDebit, SalesCreditDebitAdmin)
admin.site.register(DetailSalesCreditDebit, DetailSalesCreditDebitAdmin)
admin.site.register(TaxaMachineCard, TaxaMachineCardCardAdmin)
admin.site.register(Feriados, FeriadosAdmin)
