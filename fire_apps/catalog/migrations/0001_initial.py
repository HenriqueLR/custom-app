# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id_catalog', models.AutoField(serialize=False, verbose_name='Cod Catalog', primary_key=True, db_column=b'id_catalog')),
                ('cod_produto', models.CharField(max_length=100, null=True, verbose_name='codigo produto', db_column=b'cod_produto', blank=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('description', models.TextField(verbose_name='Descricao', db_column=b'description')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('preco_vista', models.CharField(max_length=100, verbose_name='Preco Vista', db_column=b'preco_vista')),
                ('preco_prazo', models.CharField(max_length=100, null=True, verbose_name='Preco Prazo', db_column=b'preco_prazo', blank=True)),
                ('preco_corte', models.CharField(max_length=100, null=True, verbose_name='Preco Corte', db_column=b'preco_corte', blank=True)),
                ('imagem', models.FileField(upload_to=b'', verbose_name='Imagem', db_column=b'imagem')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'catalog',
                'verbose_name': 'Catalogo',
                'verbose_name_plural': 'Catalogo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id_classification', models.AutoField(serialize=False, verbose_name='Cod Classification', primary_key=True, db_column=b'id_classification')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'classification',
                'verbose_name': 'Classifica\xe7\xe3o',
                'verbose_name_plural': 'Classifica\xe7\xe3o',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='catalog',
            name='classification',
            field=models.ForeignKey(related_name=b'catalog_classification', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'classification', blank=True, to='catalog.Classification', null=True),
            preserve_default=True,
        ),
    ]
