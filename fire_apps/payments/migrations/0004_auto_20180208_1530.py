# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20180208_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescreditdebit',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, verbose_name=b'Valor Total', max_digits=10, db_column=b'valor_total'),
        ),
    ]
