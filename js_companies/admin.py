# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django import forms
import os

from . import models


class CompanyForm(forms.ModelForm):
    def clean(self):
        image = self.cleaned_data.get('image')
        if image:
            url = image.url
            ext = os.path.splitext(url)[1].lower()
            if ext not in ['.svg', '.jpg', '.jpeg', '.png']:
                raise forms.ValidationError('Invalid file type')

    class Meta:
        model = models.Company
        exclude = []


class CompanyAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'url',
        'image',
    ]
    form = CompanyForm


admin.site.register(models.Company, CompanyAdmin)
