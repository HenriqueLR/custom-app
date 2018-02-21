# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20180208_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feriados',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_feriado', models.AutoField(serialize=False, verbose_name='Cod Feriado', primary_key=True, db_column=b'id_feriado')),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome Feriado', db_column=b'name')),
                ('dia', models.IntegerField(verbose_name=b'Dia', db_column=b'dia')),
                ('ano', models.IntegerField(verbose_name=b'Ano', db_column=b'ano')),
                ('mes', models.IntegerField(verbose_name=b'Mes', db_column=b'mes')),
            ],
            options={
                'ordering': ['mes'],
                'db_table': 'feriado',
                'verbose_name': 'Feriado',
                'verbose_name_plural': 'Feriados',
            },
            bases=(models.Model,),
        ),
    ]
