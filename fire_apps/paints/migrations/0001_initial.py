# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id_empresa', models.AutoField(serialize=False, verbose_name='Cod Empresa', primary_key=True, db_column=b'id_empresa')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nome', db_column=b'name', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
            ],
            options={
                'ordering': ['-id_empresa'],
                'db_table': 'empresas',
                'verbose_name': 'Empresas',
                'verbose_name_plural': 'Empresas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Formulas',
            fields=[
                ('id_formula', models.AutoField(serialize=False, verbose_name='Cod Sales', primary_key=True, db_column=b'id_formula')),
                ('cod_sale', models.CharField(max_length=100, verbose_name='codigo venda', db_column=b'cod_venda')),
                ('titulo', models.CharField(max_length=100, null=True, verbose_name='titulo', blank=True)),
                ('codigo', models.CharField(max_length=100, null=True, verbose_name='codigo', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('ano', models.CharField(max_length=100, null=True, verbose_name='ano', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('quantidade', models.CharField(max_length=100, null=True, verbose_name='quantidade', blank=True)),
                ('preco_venda', models.CharField(max_length=100, null=True, verbose_name='preco_venda', blank=True)),
                ('preco_custo', models.CharField(max_length=100, null=True, verbose_name='preco_custo', blank=True)),
                ('pigmentos', models.FileField(upload_to=b'', null=True, verbose_name='Pigmentos', db_column=b'pigmentos', blank=True)),
                ('empresa', models.ForeignKey(related_name=b'sales_empresas', verbose_name=b'Empresas', to='paints.Empresas')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'formulas',
                'verbose_name': 'Formulas',
                'verbose_name_plural': 'Formulas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Montadora',
            fields=[
                ('id_montadora', models.AutoField(serialize=False, verbose_name='Cod Montadora', primary_key=True, db_column=b'id_montadora')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nome', db_column=b'name', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
            ],
            options={
                'ordering': ['-id_montadora'],
                'db_table': 'montadoras',
                'verbose_name': 'Montadoras',
                'verbose_name_plural': 'Montadoras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id_tipo', models.AutoField(serialize=False, verbose_name='Cod Tipo', primary_key=True, db_column=b'id_tipo')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nome', db_column=b'name', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
            ],
            options={
                'ordering': ['-id_tipo'],
                'db_table': 'tipos',
                'verbose_name': 'Tipos',
                'verbose_name_plural': 'Tipos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='formulas',
            name='montadora',
            field=models.ForeignKey(related_name=b'sales_montadoras', verbose_name=b'Montadoras', blank=True, to='paints.Montadora', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formulas',
            name='tipo',
            field=models.ForeignKey(related_name=b'sales_tipos', verbose_name=b'Tipos', to='paints.Tipos'),
            preserve_default=True,
        ),
    ]
