#coding: utf-8

from django.shortcuts import render
from django.views.generic.list import ListView
from catalog.models import Catalog, Classification
from django.db.models import Q



class CatalogListView(ListView):

	model = Catalog
	paginate_by = 20
	template_name = 'catalog/list_catalog.html'

	def get_context_data(self, **kwargs):
		context = super(CatalogListView, self).get_context_data(**kwargs)
		context.update({'title':'Fire Tintas', 'classification':Classification.objects.all().order_by('created_at')})
		return context

	def get_queryset(self):
		qs = self.model.objects.all().order_by('-created_at')

		search = self.request.GET.get('search', '').lower()
		if search != '':
			qs = qs.filter(Q(titulo__contains=search) | Q(cod_produto__contains=search))

		select = self.request.GET.get('select', '').lower()
		if select != '' and select != 'todos':
			qs = qs.filter(classification__name=select)

		return qs

list_catalog = CatalogListView.as_view()    
