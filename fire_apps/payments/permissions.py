#coding: utf-8

from django.contrib.auth.decorators import login_required



class PermissionsGeralMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(PermissionsGeralMixin, cls).as_view())