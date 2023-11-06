# Generated by Django 2.2.19 on 2021-03-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_companies', '0004_auto_20190430_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='namespace',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Instance namespace'),
        ),
        migrations.AddField(
            model_name='company',
            name='type',
            field=models.CharField(default='js_locations.Location', max_length=100, verbose_name='Type'),
        ),
    ]
