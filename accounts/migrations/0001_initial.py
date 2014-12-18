# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def load_data(apps, schema_editor):
    call_command('loaddata', 'user_data')

def unload_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data, unload_data)
    ]
