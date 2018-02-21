# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescreditdebit',
            name='status',
            field=models.ForeignKey(related_name=b'credit_debit_status', db_column=b'status', default=1, verbose_name=b'Status Venda', to='payments.StatusCreditDebit'),
        ),
    ]
