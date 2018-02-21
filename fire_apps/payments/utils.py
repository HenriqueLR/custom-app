#coding: utf-8
import json
from payments.models import TaxaMachineCard, Feriados
from datetime import datetime, timedelta

#(100 * int(round(real_br_money_mask(obj['total'])))/int(round(total)))


def data_graph_pie(data, total):
    data_graph = []
    for obj in data:
        data_graph.append(json.load(str({'name':obj['tipo__name'],
                     'y': '{:,.1f}'.format(float((100 * int(round(obj['total']))/int(round(total))))),})))
    return data_graph


def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')


def convert_string_to_date(dt_str, format):
    return datetime.strptime(dt_str, format)


def calc_sale(valor_total, maquina, tipo, total_parc):
    taxa = TaxaMachineCard.objects.get(machinecard=maquina, tipo=tipo, count_parc=total_parc)
    total_perdido = valor_total / 100 * taxa.taxa

    data = {
        'total_perdido': total_perdido,
        'valor_calc': valor_total - total_perdido,
    }

    return data


def get_dt_process(dt, tipo, parcela=None):
    if tipo == 'hour':
        dt_format = dt + timedelta(hours=24)
        dt_process = calc_dt_weekend(dt_format)

    elif tipo == 'day':
        dt_format = dt + timedelta(days=parcela * 30)
        dt_process = calc_dt_weekend(dt_format)

    return dt_process


def calc_dt_weekend(dt_format):
    feriado = Feriados.objects.filter(dia=dt_format.day, mes=dt_format.month, ano=dt_format.year)
    weekday = dt_format.weekday()

    if weekday == 5 or weekday == 6 or feriado:
        return get_dt_process(dt_format, 'hour')

    return dt_format


def process_detail_sale(sale, parcela):
    data = {}

    if sale.tipo.pk == 2:
        data['valor_parcela'] = sale.valor_calc
        data['valor_perdido_parc'] = sale.valor_perdido_total
        data['current_parc'] = sale.total_parc
        data['data_process'] = get_dt_process(sale.created_at, 'hour')

    elif sale.tipo.pk == 1:
        data['valor_parcela'] = sale.valor_calc / sale.total_parc
        data['valor_perdido_parc'] = sale.valor_perdido_total / sale.total_parc
        data['current_parc'] = parcela
        data['data_process'] = get_dt_process(sale.created_at, 'day', parcela)

    return data