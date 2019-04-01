# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import models


class CompanyAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'url',
        'image',
    ]


admin.site.register(models.Company, CompanyAdmin)
