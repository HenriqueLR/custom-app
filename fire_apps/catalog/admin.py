#coding: utf-8

from django.contrib import admin
from catalog.models import Catalog, Classification



class ClassificationAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'created_at', 'updated_at')
	list_filter = ('name',)
	search_fields = ('name',)



class CatalogAdmin(admin.ModelAdmin):
	list_display = ('cod_produto', 'titulo', 'preco_vista', 'preco_prazo', 'preco_corte', 'classification')
	list_filter = ('titulo', 'classification')
	search_fields = ('titulo', 'description', 'cod_produto', 'preco_corte', 'preco_prazo', 'preco_vista', 'classification')



admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Classification, ClassificationAdmin)
