#coding: utf-8

import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe



class Tipos(models.Model):

	id_tipo = models.AutoField(primary_key=True, verbose_name=u'Cod Tipo', db_column='id_tipo')
	name = models.CharField(verbose_name=u'Nome', max_length=100, blank=True, 
							null=True, db_column='name', unique=True)
	description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name='Tipos'
		verbose_name_plural='Tipos'
		ordering=['-id_tipo']
		db_table='tipos'



class Montadora(models.Model):

	id_montadora = models.AutoField(primary_key=True, verbose_name=u'Cod Montadora', db_column='id_montadora')
	name = models.CharField(verbose_name=u'Nome', max_length=100, blank=True, null=True, 
							db_column='name', unique=True)
	description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name='Montadoras'
		verbose_name_plural='Montadoras'
		ordering=['-id_montadora']
		db_table='montadoras'



class Empresas(models.Model):

	id_empresa = models.AutoField(primary_key=True, verbose_name=u'Cod Empresa', db_column='id_empresa')
	name = models.CharField(verbose_name=u'Nome', max_length=100, blank=True, null=True, 
							db_column='name', unique=True)
	description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name='Empresas'
		verbose_name_plural='Empresas'
		ordering=['-id_empresa']
		db_table='empresas'



class Formulas(models.Model):

	id_formula = models.AutoField(primary_key=True, verbose_name=u'Cod Sales', db_column='id_formula')
	cod_sale = models.CharField(verbose_name=u'codigo venda', max_length=100, 
								db_column='cod_venda')
	titulo = models.CharField(verbose_name=u'titulo', max_length=100, blank=True, null=True)
	codigo = models.CharField(verbose_name=u'codigo', max_length=100, blank=True, null=True)
	tipo = models.ForeignKey(Tipos, verbose_name='Tipos', related_name='sales_tipos', null=False) 
	empresa = models.ForeignKey(Empresas, verbose_name='Empresas', related_name='sales_empresas', null=False)
	montadora = models.ForeignKey(Montadora, verbose_name='Montadoras', related_name='sales_montadoras', null=True, blank=True)
	description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')
	ano = models.CharField(verbose_name=u'ano', max_length=100, blank=True, null=True)
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
	quantidade = models.CharField(verbose_name=u'quantidade', max_length=100, blank=True, null=True)
	preco_venda = models.CharField(verbose_name=u'preco_venda', max_length=100, blank=True, null=True)
	preco_custo = models.CharField(verbose_name=u'preco_custo', max_length=100, blank=True, null=True)
	pigmentos = models.FileField(verbose_name=u'Pigmentos', db_column='pigmentos', blank=True, null=True)

	def __unicode__(self):
		return self.cod_sale

	def url(self):
		return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.pigmentos)))

	def image_tag(self):
		return mark_safe('<img src="{}"/>'.format(self.url()))
	
	image_tag.short_description = 'formula' 

	class Meta:
		verbose_name='Formulas'
		verbose_name_plural='Formulas'
		ordering=['-created_at']
		db_table='formulas'
