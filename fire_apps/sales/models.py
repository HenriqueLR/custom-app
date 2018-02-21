#coding: utf-8

from django.db import models
from sales.utils import validate_cpf



CHOICES_TYPE_SALES = (('1','A VISTA'),)


UF_CHOICES = (
    ('AC', 'Acre'),('AL', 'Alagoas'),('AP', 'Amapá'),('BA', 'Bahia'),('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),('ES', 'Espírito Santo'),('GO', 'Goiás'),('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),('MS', 'Mato Grosso do Sul'),('MT', 'Mato Grosso'),('PA', 'Pará'),
    ('PB', 'Paraíba'),('PE', 'Pernanbuco'),('PI', 'Piauí'),('PR', 'Paraná'),('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),('RO', 'Rondônia'),('RR', 'Roraima'),('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),('SE', 'Sergipe'),('SP', 'São Paulo'),('TO', 'Tocantins')
)



class DefaultFieldsModel(models.Model):
    updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
    created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
    description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')

    class Meta:
        abstract = True



class Salesman(DefaultFieldsModel):
    id_salesman = models.AutoField(primary_key=True, verbose_name=u'Cod Vendedor', db_column='id_salesman')
    phone = models.CharField(verbose_name='Telefone', db_column='phone', null=True, blank=True, max_length=100)
    name = models.CharField(verbose_name='Nome', db_column='name', unique=True, max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Vendedores'
        verbose_name_plural = 'Vendedores'
        ordering=['-created_at']
        db_table='salesman'



class Customer(DefaultFieldsModel):
	id_customer = models.AutoField(primary_key=True, verbose_name=u'Cod Cliente', db_column='id_customer')
	name = models.CharField(verbose_name='Nome', db_column='name', unique=True, max_length=100)
	cpf = models.CharField(unique=True, max_length=14, validators=[validate_cpf], null=True, blank=True)
	rua = models.CharField(verbose_name='Rua', db_column='rua', max_length=100, blank=True, null=True)
	numero = models.CharField(verbose_name='Numero', db_column='numero', max_length=10, blank=True, null=True)
	bairro = models.CharField(verbose_name='Bairro', db_column='bairro', max_length=100, blank=True, null=True)
	cidade = models.CharField(verbose_name='Cidade', db_column='cidade', max_length=100, blank=True, null=True)
	estado = models.CharField(verbose_name='Estado', db_column='estado', max_length=2,
								blank=True, null=True, choices=UF_CHOICES)
	email = models.EmailField(verbose_name=u'E-mail', unique=True, null=True, blank=True, db_column='email')
	phone = models.CharField(verbose_name='Telefone', db_column='phone',
								max_length=100, blank=True, null=True)

	def __unicode__(self):
		return u'%s - %s' % (self.name, self.cpf)

	class Meta:
		verbose_name = 'Clientes'
		verbose_name_plural = 'Clientes'
		ordering=['-created_at']
		db_table='customer'



class Sales(DefaultFieldsModel):
	id_sales = models.AutoField(primary_key=True, verbose_name=u'Cod Venda', db_column='id_sales')
	cod_venda = models.CharField(verbose_name='Cod Venda', db_column='cod_venda', max_length=100, unique=True)
	salesman = models.ForeignKey(Salesman, verbose_name='Vendedor',
									related_name='sales_salesman', db_column='salesman')
	type_sales = models.CharField(choices=CHOICES_TYPE_SALES, max_length=10,
									verbose_name=u'Tipo Venda', db_column='type_sales')
	customer = models.ForeignKey(Customer, verbose_name='Cliente',
									related_name='sales_customer', db_column='customer')

	def __unicode__(self):
		return self.cod_venda

	class Meta:
		verbose_name = 'Vendas'
		verbose_name_plural = 'Vendas'
		ordering=['-created_at']
		db_table='sales'
