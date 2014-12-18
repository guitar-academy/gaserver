# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def load_data(apps, schema_editor):
    call_command('loaddata', 'training_data')

def unload_data(apps, schema_editor):

    Song = apps.get_model('training', 'Song')
    Skill = apps.get_model('training', 'Skill')
    WarmUp = apps.get_model('training', 'WarmUp')
    SongSkill = apps.get_model('training', 'SongSkill')
    WarmUpSong = apps.get_model('training', 'WarmUpSong')

    Song.objects.all().delete()
    Skill.objects.all().delete()
    WarmUp.objects.all().delete()
    SongSkill.objects.all().delete()
    WarmUpSong.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data, unload_data)
    ]
