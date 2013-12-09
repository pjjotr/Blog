# encoding: utf8
from django.db import models, migrations
import django.contrib.sites.models


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('domain', models.CharField(max_length=100, verbose_name=u'domain name', validators=[django.contrib.sites.models._simple_domain_name_validator]),), ('name', models.CharField(max_length=50, verbose_name=u'display name'),)],
            bases = (models.Model,),
            options = {u'ordering': (u'domain',), u'db_table': u'django_site', u'verbose_name': u'site', u'verbose_name_plural': u'sites'},
            name = 'Site',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('size', models.CharField(max_length=15, verbose_name='Rozmiar'),), ('age', models.TextField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Chujostwo',
        ),
    ]
