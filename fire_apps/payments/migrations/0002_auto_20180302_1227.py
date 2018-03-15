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
            name='created_at',
            field=models.DateTimeField(verbose_name='Criado em', db_column=b'created_at'),
        ),
    ]
