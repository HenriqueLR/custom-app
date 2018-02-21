#coding: utf-8

from django.contrib import admin
from sales.models import Salesman, Customer, Sales



class SalesmanAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'atualizado', 'criado', 'description')
	fields = ['name', 'description', 'phone']
	search_fields = ('name',)

	def criado(self, obj):
		return obj.created_at.strftime('%d/%m/%Y %H:%M:%S')

	def atualizado(self, obj):
		return obj.updated_at.strftime('%d/%m/%Y %H:%M:%S')



class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'cpf', 'cidade', 'estado', 'email', 'phone',
					'description', 'criado', 'atualizado')
	fields = ['name', 'cpf', 'rua', 'numero', 'bairro', 'cidade', 'estado',
			  'email', 'phone', 'description']
	search_fields = ('name', 'cpf', 'cidade', 'estado', 'email', 'phone')
	list_filter = ('cidade', 'estado')

	def criado(self, obj):
		return obj.created_at.strftime('%d/%m/%Y %H:%M:%S')

	def atualizado(self, obj):
		return obj.updated_at.strftime('%d/%m/%Y %H:%M:%S')



class SalesAdmin(admin.ModelAdmin):
	list_display = ('cod_venda', 'salesman', 'type_sales', 'customer',
					'description', 'atualizado', 'criado')
	fields = ['cod_venda', 'salesman', 'type_sales', 'customer', 'description']
	search_fields = ('cod_venda', 'salesman__name', 'customer__name', 'customer__cpf', 'customer__phone')
	list_filter = ('salesman',)

	def criado(self, obj):
		return obj.created_at.strftime('%d/%m/%Y %H:%M:%S')

	def atualizado(self, obj):
		return obj.updated_at.strftime('%d/%m/%Y %H:%M:%S')



admin.site.register(Salesman, SalesmanAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sales, SalesAdmin)
