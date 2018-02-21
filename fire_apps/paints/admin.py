#coding: utf-8

from django.contrib import admin
from paints.models import Tipos, Montadora, Empresas, Formulas



class TiposAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ['name',]	



class MontadoraAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ['name',]	



class EmpresasAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ['name',]



class FormulasAdmin(admin.ModelAdmin):
	list_display = ('cod_sale', 'empresa', 'titulo', 'codigo', 'tipo', 'montadora', 'criado')
	list_filter = ('tipo', 'montadora')
	fields = ['cod_sale', 'titulo', 'codigo', 'tipo', 'empresa', 'montadora', 'description', 
			  'ano', 'quantidade', 'preco_venda', 'preco_custo', 'image_tag', 'pigmentos']
	search_fields = ('titulo', 'cod_sale', 'empresa__name', 'tipo__name', 'montadora__name')
	readonly_fields = ('image_tag',)


	def criado(self, obj):
		return obj.created_at.strftime('%d/%m/%Y %H:%M:%S')

	def atualizado(self, obj):
		return obj.updated_at.strftime('%d/%m/%Y %H:%M:%S')



admin.site.register(Tipos, TiposAdmin)
admin.site.register(Montadora, MontadoraAdmin)
admin.site.register(Empresas, EmpresasAdmin)
admin.site.register(Formulas, FormulasAdmin)
