#coding: utf-8

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from sales.models import Customer
from sales.form import CustomerForm
from django.db.models import Q



class CustomerAddView(CreateView):

    model = Customer
    form_class = CustomerForm
    template_name = 'sales/customer/add_customer.html'
    success_url = reverse_lazy('sales:list_customer')

    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, 'Cliente adicionado com sucesso')
        except Exception as Error:
            messages.error(self.request, 'Erro ao cadastrar o cliente')
        return HttpResponseRedirect(self.success_url)



class CustomerListView(ListView):

    model = Customer
    paginate_by = 10
    template_name = 'sales/customer/list_customer.html'


add_customer = CustomerAddView.as_view()
list_customer = CustomerListView.as_view()
