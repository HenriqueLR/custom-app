#coding: utf-8

import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
# Create your models here.



class Classification(models.Model):

	id_classification = models.AutoField(primary_key=True, verbose_name=u'Cod Classification', db_column='id_classification')
	name = models.CharField(verbose_name=u'Nome', max_length=100)
	description = models.TextField(db_column='description', verbose_name=u'Descricao', null=True, blank=True)
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name='Classificação'
		verbose_name_plural='Classificação'
		ordering=['-created_at']
		db_table='classification'			


class Catalog(models.Model):

	id_catalog = models.AutoField(primary_key=True, verbose_name=u'Cod Catalog', db_column='id_catalog')
	cod_produto = models.CharField(verbose_name=u'codigo produto', max_length=100, 
								db_column='cod_produto', blank=True, null=True)
	titulo = models.CharField(verbose_name=u'titulo', max_length=100)
	description = models.TextField(db_column='description', verbose_name=u'Descricao')
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
	preco_vista = models.CharField(verbose_name=u'Preco Vista', max_length=100, db_column='preco_vista')
	preco_prazo = models.CharField(verbose_name=u'Preco Prazo', max_length=100, blank=True, null=True, 
									db_column='preco_prazo')
	preco_corte = models.CharField(verbose_name=u'Preco Corte', max_length=100, blank=True, null=True, 
									db_column='preco_corte')
	imagem = models.FileField(verbose_name=u'Imagem', db_column='imagem')
	classification = models.ForeignKey(Classification, verbose_name='classification', blank=True,
										related_name='catalog_classification', null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.titulo

	def url(self):
		return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.imagem)))

	def image_tag(self):
		return mark_safe('<img src="{}"/>'.format(self.url()))
	
	image_tag.short_description = 'imagem' 

	class Meta:
		verbose_name='Catalogo'
		verbose_name_plural='Catalogo'
		ordering=['-created_at']
		db_table='catalog'	
