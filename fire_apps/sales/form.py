#coding: utf-8

from django import forms
from sales.models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'