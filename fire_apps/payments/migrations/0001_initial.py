# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailSalesCreditDebit',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_detail_sales_credit_debit', models.AutoField(serialize=False, verbose_name='Cod Detail Credito Debito', primary_key=True, db_column=b'id_detail_sales_credit_debit')),
                ('current_parc', models.IntegerField(default=1, verbose_name=b'Parcela Corrente', db_column=b'current_parc')),
                ('valor_parcela', models.DecimalField(default=0, decimal_places=2, verbose_name=b'Valor Parcela', max_digits=10, db_column=b'valor_parcela')),
                ('valor_perdido_parc', models.DecimalField(default=0, decimal_places=2, verbose_name=b'Valor Perdido Parcelado', max_digits=10, db_column=b'valor_perdido_parc')),
                ('data_process', models.DateTimeField(verbose_name='Data de Processamento', db_column=b'data_process')),
                ('status_detail', models.BooleanField(default=0, verbose_name='Status', db_column=b'status_detail')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'detail_sale_credit_debit',
                'verbose_name': 'Detail Sale Credit Debit',
                'verbose_name_plural': 'Detail Sale Credit Debit',
            },
        ),
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
        ),
        migrations.CreateModel(
            name='MachineCard',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_machine_card', models.AutoField(serialize=False, verbose_name='Cod Machine Card', primary_key=True, db_column=b'id_machine_card')),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome Maquina Cart\xc3\xa3o', db_column=b'name')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'machine_card',
                'verbose_name': 'Machine Card',
                'verbose_name_plural': 'Machine Card',
            },
        ),
        migrations.CreateModel(
            name='SalesCreditDebit',
            fields=[
                ('id_sales_credit_debit', models.AutoField(serialize=False, verbose_name='Cod Venda Credito Debito', primary_key=True, db_column=b'id_sales_credit_debit')),
                ('cod_venda', models.TextField(null=True, verbose_name='Codigo da Venda', db_column=b'cod_venda', blank=True)),
                ('total_parc', models.IntegerField(default=1, verbose_name=b'Total Parcelas', db_column=b'total_parc')),
                ('valor_total', models.DecimalField(decimal_places=2, verbose_name=b'Valor Total', max_digits=10, db_column=b'valor_total')),
                ('valor_calc', models.DecimalField(default=0, decimal_places=2, verbose_name=b'Valor Calculado', max_digits=10, db_column=b'valor_calc')),
                ('valor_perdido_total', models.DecimalField(default=0, decimal_places=2, verbose_name=b'Valor Perdido Total', max_digits=10, db_column=b'valor_perdido_total')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('machinecard', models.ForeignKey(related_name='sales_credit_debit_machinecard', db_column=b'machinecard', verbose_name=b'Maquina de Cart\xc3\xa3o', to='payments.MachineCard')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'sales_credit_debit',
                'verbose_name': 'Vendas Credito Debito',
                'verbose_name_plural': 'Vendas Credito Debito',
            },
        ),
        migrations.CreateModel(
            name='StatusCreditDebit',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_status_credit_debit', models.AutoField(serialize=False, verbose_name='Cod Status Credit Debit', primary_key=True, db_column=b'id_status_credit_debit')),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome Status', db_column=b'name')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'status_credit_debit',
                'verbose_name': 'Status Credit Debit',
                'verbose_name_plural': 'Status Credit Debit',
            },
        ),
        migrations.CreateModel(
            name='TaxaMachineCard',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_taxa_machine_card', models.AutoField(serialize=False, verbose_name='Cod Taxa Machine Card', primary_key=True, db_column=b'id_taxa_machine_card')),
                ('count_parc', models.IntegerField(default=1, verbose_name=b'Vezes', db_column=b'count_parc')),
                ('taxa', models.DecimalField(default=0, decimal_places=2, verbose_name=b'Taxa', max_digits=10, db_column=b'taxa')),
                ('machinecard', models.ForeignKey(related_name='taxa_machine_card', db_column=b'machinecard', verbose_name=b'Maquina Cart\xc3\xa3o', to='payments.MachineCard')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'taxa_machine_card',
                'verbose_name': 'Taxa Maquina Cartao',
                'verbose_name_plural': 'Taxa Maquina Cartao',
            },
        ),
        migrations.CreateModel(
            name='TipoCreditDebit',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
                ('description', models.TextField(null=True, verbose_name='Descricao', db_column=b'description', blank=True)),
                ('id_tipo_credit_debit', models.AutoField(serialize=False, verbose_name='Cod Tipo Credit Debit', primary_key=True, db_column=b'id_tipo_credit_debit')),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome Tipo', db_column=b'name')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'tipo_credit_debit',
                'verbose_name': 'Tipo Credit Debit',
                'verbose_name_plural': 'Tipo Credit Debit',
            },
        ),
        migrations.AddField(
            model_name='taxamachinecard',
            name='tipo',
            field=models.ForeignKey(related_name='taxa_machine_card_tipo', db_column=b'tipo', verbose_name=b'Tipo Taxa', to='payments.TipoCreditDebit'),
        ),
        migrations.AddField(
            model_name='salescreditdebit',
            name='status',
            field=models.ForeignKey(related_name='credit_debit_status', db_column=b'status', default=1, verbose_name=b'Status Venda', to='payments.StatusCreditDebit'),
        ),
        migrations.AddField(
            model_name='salescreditdebit',
            name='tipo',
            field=models.ForeignKey(related_name='sales_credit_debit_tipo', db_column=b'tipo', verbose_name=b'Tipo Venda', to='payments.TipoCreditDebit'),
        ),
        migrations.AddField(
            model_name='detailsalescreditdebit',
            name='sale_credit_debit',
            field=models.ForeignKey(related_name='detail_credit_debit', db_column=b'sale_credit_debit', verbose_name=b'Cod Sale Credit Debit', to='payments.SalesCreditDebit'),
        ),
    ]
