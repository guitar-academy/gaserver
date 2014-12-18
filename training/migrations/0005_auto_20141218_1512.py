# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20141218_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='skills',
            field=models.ManyToManyField(through='training.SongSkill', related_name='songs', blank=True, to='training.Skill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='warmup',
            name='songs',
            field=models.ManyToManyField(through='training.WarmUpSong', related_name='warmups', to='training.Song'),
            preserve_default=True,
        ),
    ]
