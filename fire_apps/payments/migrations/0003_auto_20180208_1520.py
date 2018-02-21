# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20180208_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescreditdebit',
            name='status',
            field=models.ForeignKey(related_name=b'credit_debit_status', db_column=b'status', default=1, verbose_name=b'Status Venda', to='payments.StatusCreditDebit'),
        ),
    ]
