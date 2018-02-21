#coding: utf-8

from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from payments.models import SalesCreditDebit, DetailSalesCreditDebit
from datetime import datetime


@task(name="hello_word")
def hello():
    sales = SalesCreditDebit.objects.filter(status__name='aberto')
    for sale in sales:
        details = DetailSalesCreditDebit.objects.filter(sale_credit_debit=sale, status_detail=False)
        if details.exists():
            for detail in details:
                dt_today = datetime.today()
                if dt_today > detail.data_process:
                    obj = DetailSalesCreditDebit.objects.get(pk=detail.pk)
                    obj.status_detail = True
                    obj.save()
        else:
            obj = SalesCreditDebit.objects.filter(pk=sale.pk).update(status=2)