# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20141218_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='skills',
            field=models.ManyToManyField(through='training.SongSkill', to='training.Skill', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='warmup',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='songskill',
            unique_together=set([('song', 'skill')]),
        ),
    ]
