# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(_('Company Name'), max_length=255)
    url = models.CharField(_('Page URL'), max_length=255,
        null=True, blank=True)
    image = FilerImageField(verbose_name=_('image'),
        null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
