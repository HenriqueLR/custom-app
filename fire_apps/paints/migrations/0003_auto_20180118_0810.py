# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0002_auto_20180112_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulas',
            name='cod_sale',
            field=models.CharField(max_length=100, verbose_name='codigo venda', db_column=b'cod_venda'),
        ),
    ]
