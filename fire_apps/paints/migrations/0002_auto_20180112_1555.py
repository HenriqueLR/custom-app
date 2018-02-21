# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='name',
            field=models.CharField(null=True, db_column=b'name', max_length=100, blank=True, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='formulas',
            name='cod_sale',
            field=models.CharField(unique=True, max_length=100, verbose_name='codigo venda', db_column=b'cod_venda'),
        ),
        migrations.AlterField(
            model_name='montadora',
            name='name',
            field=models.CharField(null=True, db_column=b'name', max_length=100, blank=True, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='tipos',
            name='name',
            field=models.CharField(null=True, db_column=b'name', max_length=100, blank=True, unique=True, verbose_name='Nome'),
        ),
    ]
