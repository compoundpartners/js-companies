# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.utils.text import slugify

from filer.fields.file import FilerFileField
from sortedm2m.fields import SortedManyToManyField


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(_('Company Name'), max_length=255)
    url = models.CharField(_('Page URL'), max_length=255,
        null=True, blank=True)
    image = FilerFileField(verbose_name=_('image'),
        null=True, blank=True, on_delete=models.SET_NULL)

    articles = SortedManyToManyField('aldryn_newsblog.Article', verbose_name=_('articles'), related_name='companies', blank=True)
    newsblogjsrelatedplugins = SortedManyToManyField('aldryn_newsblog.NewsBlogJSRelatedPlugin', verbose_name=_('newsblogjsrelatedplugins'), related_name='related_companies', blank=True)
    events = SortedManyToManyField('js_events.Event', verbose_name=_('events'), related_name='companies', blank=True)
    people = SortedManyToManyField('aldryn_people.Person', verbose_name=_('people'), related_name='companies', blank=True)
    relatedpeopleplugin = SortedManyToManyField('aldryn_people.RelatedPeoplePlugin', verbose_name=_('relatedpeopleplugin'), related_name='related_companies', blank=True)
    services = SortedManyToManyField('js_services.Service', verbose_name=_('services'), related_name='companies', blank=True)
    relatedservicesplugin = SortedManyToManyField('js_services.RelatedServicesPlugin', verbose_name=_('relatedservicesplugin'), related_name='related_companies', blank=True)

    #app config fields and mithods
    type = models.CharField(
        _('Type'),
        max_length=100,
        default='js_locations.Location',
    )
    namespace = models.CharField(
        _('Instance namespace'),
        #default=None,
        max_length=100,
        unique=True,
        blank=True,
        null=True,
    )

    cmsapp = None

    def save(self, *args, **kwargs):
        self.type = '%s.%s' % (
            self.__class__.__module__, self.__class__.__name__)
        if not self.namespace:
            self.namespace = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
