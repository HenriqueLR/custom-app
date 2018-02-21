#coding: utf-8

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from payments.models import SalesCreditDebit, DetailSalesCreditDebit, StatusCreditDebit, TipoCreditDebit
from payments.form import SalesCreditDebitForm
from payments.utils import data_graph_pie, convert_string_to_date
from payments.permissions import PermissionsGeralMixin
from django.db.models import Count, Min, Sum, Avg
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime



class DashListView(PermissionsGeralMixin, ListView):

    model = SalesCreditDebit
    paginate_by = 20
    template_name = 'payments/dash_payments.html'

    def get_context_data(self, **kwargs):
        context = super(DashListView, self).get_context_data(**kwargs)

        total_credit_debit = self.model.objects.values('tipo__name')\
                               .annotate(total=Sum('valor_calc'))\
                               .order_by('-tipo__name')
        credit_detail = self.model.objects.filter(tipo__name='crédito')\
                        .values('tipo__name', 'status__name')\
                        .annotate(total=Sum('valor_calc'))\
                        .order_by('-tipo__name')
        debit_detail = self.model.objects.filter(tipo__name='débito')\
                        .values('tipo__name','status__name')\
                        .annotate(total=Sum('valor_calc'))\
                        .order_by('-tipo__name')

        dt = self.request.GET.get('range_dt', '')
        if dt != '':
            dt_start, dt_end = dt.split('-')
            dt_start = convert_string_to_date(dt_start.strip()+' 00:00:00', '%d/%m/%Y %H:%M:%S')
            dt_end = convert_string_to_date(dt_end.strip()+' 23:59:59', '%d/%m/%Y %H:%M:%S')

            total_credit_debit = total_credit_debit.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                                                           created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))
            total = self.model.objects.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                                              created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))\
                                              .aggregate(Sum('valor_calc'))['valor_calc__sum'] or 0
            credit_total = self.model.objects.filter(tipo__name='crédito',
                                                     created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                                                     created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))\
                                                     .aggregate(Sum('valor_calc'))['valor_calc__sum'] or 0
            credit_detail = credit_detail.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                                                 created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))
            debit_total = self.model.objects.filter(tipo__name='débito',
                                                     created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                                                     created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))\
                           .aggregate(Sum('valor_calc'))['valor_calc__sum'] or 0
            debit_detail = debit_detail.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                                                created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            total = self.model.objects.aggregate(Sum('valor_calc'))['valor_calc__sum'] or 0
            credit_total = self.model.objects.filter(tipo__name='crédito')\
                            .aggregate(Sum('valor_calc'))['valor_calc__sum'] or 0
            debit_total = self.model.objects.filter(tipo__name='débito')\
                            .aggregate(Sum('valor_calc'))['valor_calc__sum'] or 0

        data = {
            'total_credit_debit': total_credit_debit,
            'total': total,
            'title':'Fire Tintas',
            'credit_total': credit_total,
            'credit_detail': credit_detail,
            'debit_total': debit_total,
            'debit_detail': debit_detail,
            'status_list': StatusCreditDebit.objects.all(),
            'tipo_list': TipoCreditDebit.objects.all(),
        }
        context.update(data)
        return context

    def get_queryset(self):
        qs = self.model.objects.all().order_by('-created_at')

        status = self.request.GET.get('status', '').lower()
        if status != '' and status != 'todos':
            qs = qs.filter(status__name=status)

        tipo = self.request.GET.get('tipo', '').lower()
        if tipo != '' and tipo != 'todos':
            qs = qs.filter(tipo__name=tipo)

        dt = self.request.GET.get('range_dt', '')
        if dt != '':
            dt_start, dt_end = dt.split('-')
            dt_start = convert_string_to_date(dt_start.strip()+' 00:00:00', '%d/%m/%Y %H:%M:%S')
            dt_end = convert_string_to_date(dt_end.strip()+' 23:59:59', '%d/%m/%Y %H:%M:%S')
            qs = qs.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                            created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))

        return qs



class CrediDebitListView(PermissionsGeralMixin, ListView):

    model = SalesCreditDebit
    paginate_by = 30
    template_name = 'payments/list_lancamentos.html'

    def get_context_data(self, **kwargs):
        context = super(CrediDebitListView, self).get_context_data(**kwargs)
        data = {
            'status_list': StatusCreditDebit.objects.all(),
            'tipo_list': TipoCreditDebit.objects.all(),
        }
        context.update(data)
        return context


    def get_queryset(self):
        qs = self.model.objects.all().order_by('-created_at')

        status = self.request.GET.get('status', '').lower()
        if status != '' and status != 'todos':
            qs = qs.filter(status__name=status)

        tipo = self.request.GET.get('tipo', '').lower()
        if tipo != '' and tipo != 'todos':
            qs = qs.filter(tipo__name=tipo)

        dt = self.request.GET.get('range_dt', '')
        if dt != '':
            dt_start, dt_end = dt.split('-')
            dt_start = convert_string_to_date(dt_start.strip()+' 00:00:00', '%d/%m/%Y %H:%M:%S')
            dt_end = convert_string_to_date(dt_end.strip()+' 23:59:59', '%d/%m/%Y %H:%M:%S')
            qs = qs.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                            created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))

        return qs



@login_required
def add_lancamentos(request):
    form_sale = SalesCreditDebitForm(request.POST or None)

    if form_sale.is_valid():
        form_sale.save()
        messages.success(request, 'Laçamento adicionado com sucesso')
        return HttpResponseRedirect(reverse_lazy('payments:list_lancamentos'))

    context = {'form_sale':form_sale,}

    return render(request, 'payments/add_lancamento.html', context)



class DebitCreditDeleteView(PermissionsGeralMixin, DeleteView):

    model = SalesCreditDebit
    template_name = 'payments/credit_debit_confirm_delete.html'
    success_url = reverse_lazy('payments:list_lancamentos')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, 'Lançamento de débito apagado com sucesso')
        except Exception as Error:
            messages.error(self.request, 'Ocorreu um erro ao apagar o lançamento, tente novamente')
        return HttpResponseRedirect(self.success_url)



@login_required
def detail_credit_debit(request, pk):
    context = {
        'obj': SalesCreditDebit.objects.filter(pk=pk),
        'detail_credit_debit': DetailSalesCreditDebit.objects.filter(sale_credit_debit_id=pk)
    }

    return render(request, 'payments/credit_debit_detail.html', context)



def check_payments(request):
    sales = SalesCreditDebit.objects.filter(status__name='aberto')
    for sale in sales:
        details = DetailSalesCreditDebit.objects.filter(sale_credit_debit=sale, status_detail=False)
        if details.exists():
            for detail in details:
                dt_today = datetime.today()
                if dt_today > detail.data_process:
                    obj = DetailSalesCreditDebit.objects.get(pk=detail.pk)
                    obj.status_detail = True
                    obj.save()
        else:
            obj = SalesCreditDebit.objects.filter(pk=sale.pk).update(status=2)

    return HttpResponse('ok')

list_lancamentos = CrediDebitListView.as_view()
dash_payments = DashListView.as_view()
delete_credit_debit = DebitCreditDeleteView.as_view()
