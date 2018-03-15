#coding: utf-8

from django import forms
from payments.models import SalesCreditDebit, DetailSalesCreditDebit
from payments.utils import calc_sale, process_detail_sale



class SalesCreditDebitForm(forms.ModelForm):

    def save(self, commit=True):
        credit_debit = super(SalesCreditDebitForm, self).save(commit=False)

        if commit:

            data_sale = calc_sale(credit_debit.valor_total,
                             credit_debit.machinecard,
                             credit_debit.tipo,
                             credit_debit.total_parc)

            credit_debit.valor_perdido_total = data_sale['total_perdido']
            credit_debit.valor_calc = data_sale['valor_calc']
            credit_debit.save()

            for parcela in range(1, credit_debit.total_parc +1):
                data_detail_sale = process_detail_sale(credit_debit, parcela)
                detail_sale = DetailSalesCreditDebit(sale_credit_debit=credit_debit,
                                                     valor_parcela=data_detail_sale['valor_parcela'],
                                                     valor_perdido_parc=data_detail_sale['valor_perdido_parc'],
                                                     data_process=data_detail_sale['data_process'],
                                                     current_parc=data_detail_sale['current_parc'])
                detail_sale.save()

        return credit_debit

    class Meta:
        model = SalesCreditDebit
        fields = '__all__'
        exclude = ['valor_calc', 'valor_perdido_total', 'status']