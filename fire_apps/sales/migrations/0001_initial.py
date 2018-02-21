# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sales.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_customer', models.AutoField(serialize=False, verbose_name='Cod Cliente', primary_key=True, db_column=b'id_customer')),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'Nome', db_column=b'name')),
                ('cpf', models.CharField(blank=True, max_length=14, unique=True, null=True, validators=[sales.utils.validate_cpf])),
                ('rua', models.CharField(max_length=100, null=True, verbose_name=b'Rua', db_column=b'rua', blank=True)),
                ('numero', models.CharField(max_length=10, null=True, verbose_name=b'Numero', db_column=b'numero', blank=True)),
                ('bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro', db_column=b'bairro', blank=True)),
                ('cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade', db_column=b'cidade', blank=True)),
                ('estado', models.CharField(db_column=b'estado', choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amap\xc3\xa1'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maran\xc3\xa3o'), (b'MG', b'Minas Gerais'), (b'MS', b'Mato Grosso do Sul'), (b'MT', b'Mato Grosso'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PE', b'Pernanbuco'), (b'PI', b'Piau\xc3\xad'), (b'PR', b'Paran\xc3\xa1'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'RS', b'Rio Grande do Sul'), (b'SC', b'Santa Catarina'), (b'SE', b'Sergipe'), (b'SP', b'S\xc3\xa3o Paulo'), (b'TO', b'Tocantins')], max_length=2, blank=True, null=True, verbose_name=b'Estado')),
                ('email', models.EmailField(null=True, db_column=b'email', max_length=75, blank=True, unique=True, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=100, null=True, verbose_name=b'Telefone', db_column=b'phone', blank=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'customer',
                'verbose_name': 'Clientes',
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_sales', models.AutoField(serialize=False, verbose_name='Cod Venda', primary_key=True, db_column=b'id_sales')),
                ('cod_venda', models.CharField(unique=True, max_length=100, verbose_name=b'Cod Venda', db_column=b'cod_venda')),
                ('type_sales', models.CharField(max_length=10, verbose_name='Tipo Venda', db_column=b'type_sales', choices=[(b'1', b'A VISTA')])),
                ('customer', models.ForeignKey(related_name=b'sales_customer', db_column=b'customer', verbose_name=b'Cliente', to='sales.Customer')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'sales',
                'verbose_name': 'Vendas',
                'verbose_name_plural': 'Vendas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_salesman', models.AutoField(serialize=False, verbose_name='Cod Vendedor', primary_key=True, db_column=b'id_salesman')),
                ('phone', models.CharField(max_length=100, null=True, verbose_name=b'Telefone', db_column=b'phone', blank=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'Nome', db_column=b'name')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'salesman',
                'verbose_name': 'Vendedores',
                'verbose_name_plural': 'Vendedores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sales',
            name='salesman',
            field=models.ForeignKey(related_name=b'sales_salesman', db_column=b'salesman', verbose_name=b'Vendedor', to='sales.Salesman'),
            preserve_default=True,
        ),
    ]
