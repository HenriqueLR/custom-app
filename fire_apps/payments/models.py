#coding: utf-8

from django.db import models



class DefaultFieldsModel(models.Model):
    updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
    created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
    description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')

    class Meta:
        abstract = True



class StatusCreditDebit(DefaultFieldsModel):
    id_status_credit_debit = models.AutoField(primary_key=True, verbose_name=u'Cod Status Credit Debit',
                                                db_column='id_status_credit_debit')
    name = models.CharField(verbose_name='Nome Status', db_column='name', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Status Credit Debit'
        verbose_name_plural = 'Status Credit Debit'
        ordering=['-created_at']
        db_table='status_credit_debit'



class MachineCard(DefaultFieldsModel):
    id_machine_card = models.AutoField(primary_key=True, verbose_name=u'Cod Machine Card',
                                                db_column='id_machine_card')
    name = models.CharField(verbose_name='Nome Maquina Cartão', db_column='name', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Machine Card'
        verbose_name_plural = 'Machine Card'
        ordering=['-created_at']
        db_table='machine_card'



class TipoCreditDebit(DefaultFieldsModel):
    id_tipo_credit_debit = models.AutoField(primary_key=True, verbose_name=u'Cod Tipo Credit Debit',
                                                db_column='id_tipo_credit_debit')
    name = models.CharField(verbose_name='Nome Tipo', db_column='name', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo Credit Debit'
        verbose_name_plural = 'Tipo Credit Debit'
        ordering=['-created_at']
        db_table='tipo_credit_debit'



class TaxaMachineCard(DefaultFieldsModel):
    id_taxa_machine_card = models.AutoField(primary_key=True, verbose_name=u'Cod Taxa Machine Card',
                                                db_column='id_taxa_machine_card')
    machinecard = models.ForeignKey(MachineCard, verbose_name='Maquina Cartão',
                                    related_name='taxa_machine_card', db_column='machinecard')
    count_parc = models.IntegerField(verbose_name='Vezes', db_column='count_parc', default=1)
    taxa = models.DecimalField(verbose_name='Taxa', db_column='taxa',
                                        max_digits=10, decimal_places=2, default=0)
    tipo = models.ForeignKey(TipoCreditDebit, verbose_name='Tipo Taxa',
                                    related_name='taxa_machine_card_tipo', db_column='tipo')

    def __unicode__(self):
        return self.machinecard.name

    class Meta:
        verbose_name = 'Taxa Maquina Cartao'
        verbose_name_plural = 'Taxa Maquina Cartao'
        ordering=['-created_at']
        db_table='taxa_machine_card'



class SalesCreditDebit(DefaultFieldsModel):
    id_sales_credit_debit = models.AutoField(primary_key=True, verbose_name=u'Cod Venda Credito Debito',
                                                db_column='id_sales_credit_debit')
    status = models.ForeignKey(StatusCreditDebit, verbose_name='Status Venda', default=1,
                                related_name='credit_debit_status', db_column='status')
    tipo = models.ForeignKey(TipoCreditDebit, verbose_name='Tipo Venda',
                                    related_name='sales_credit_debit_tipo', db_column='tipo')
    cod_venda = models.TextField(db_column='cod_venda', blank=True, null=True, verbose_name=u'Codigo da Venda')
    machinecard = models.ForeignKey(MachineCard, verbose_name='Maquina de Cartão',
                                    related_name='sales_credit_debit_machinecard', db_column='machinecard')
    total_parc = models.IntegerField(verbose_name='Total Parcelas', db_column='total_parc', default=1)
    valor_total = models.DecimalField(verbose_name='Valor Total', db_column='valor_total',
                                        max_digits=10, decimal_places=2)
    valor_calc = models.DecimalField(verbose_name='Valor Calculado', db_column='valor_calc',
                                        max_digits=10, decimal_places=2, default=0)
    valor_perdido_total = models.DecimalField(verbose_name='Valor Perdido Total', db_column='valor_perdido_total',
                                                max_digits=10, decimal_places=2, default=0)

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.id_sales_credit_debit, self.status, self.tipo, self.total_parc)

    @models.permalink
    def get_delete_credit_debit(self):
        return('payments:delete_credit_debit', [int(self.pk)], {})

    @models.permalink
    def get_absolute_url(self):
        return('payments:detail_credit_debit', [int(self.pk)], {})


    class Meta:
        verbose_name = 'Vendas Credito Debito'
        verbose_name_plural = 'Vendas Credito Debito'
        ordering=['-created_at']
        db_table='sales_credit_debit'



class DetailSalesCreditDebit(DefaultFieldsModel):
    id_detail_sales_credit_debit = models.AutoField(primary_key=True, verbose_name=u'Cod Detail Credito Debito',
                                                        db_column='id_detail_sales_credit_debit')
    sale_credit_debit = models.ForeignKey(SalesCreditDebit, verbose_name='Cod Sale Credit Debit',
                                    related_name='detail_credit_debit', db_column='sale_credit_debit')
    current_parc = models.IntegerField(verbose_name='Parcela Corrente', db_column='current_parc', default=1)
    valor_parcela = models.DecimalField(verbose_name='Valor Parcela', db_column='valor_parcela',
                                        max_digits=10, decimal_places=2, default=0)
    valor_perdido_parc = models.DecimalField(verbose_name='Valor Perdido Parcelado', db_column='valor_perdido_parc',
                                                max_digits=10, decimal_places=2, default=0)
    data_process = models.DateTimeField(verbose_name=u'Data de Processamento', db_column='data_process')

    status_detail = models.BooleanField(verbose_name=u'Status', db_column='status_detail', blank=True, default=0)

    def __unicode__(self):
        return u'%s - %s' % (self.sale_credit_debit, self.valor_parcela)

    class Meta:
        verbose_name = 'Detail Sale Credit Debit'
        verbose_name_plural = 'Detail Sale Credit Debit'
        ordering=['-created_at']
        db_table='detail_sale_credit_debit'



class Feriados(DefaultFieldsModel):
    id_feriado = models.AutoField(primary_key=True, verbose_name=u'Cod Feriado', db_column='id_feriado')
    name = models.CharField(verbose_name='Nome Feriado', db_column='name', max_length=100)
    dia = models.IntegerField(verbose_name='Dia', db_column='dia')
    ano = models.IntegerField(verbose_name='Ano', db_column='ano')
    mes = models.IntegerField(verbose_name='Mes', db_column='mes')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Feriado'
        verbose_name_plural = 'Feriados'
        ordering=['mes']
        db_table='feriado'
