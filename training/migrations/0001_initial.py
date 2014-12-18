# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('notation', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SongSkill',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('skill', models.ForeignKey(to='training.Skill')),
                ('song', models.ForeignKey(to='training.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WarmUp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WarmUpSong',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
                ('song', models.ForeignKey(to='training.Song')),
                ('warm_up', models.ForeignKey(to='training.WarmUp')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='warmup',
            name='entries',
            field=models.ManyToManyField(to='training.Song', through='training.WarmUpSong'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='skills',
            field=models.ManyToManyField(to='training.Skill', through='training.SongSkill'),
            preserve_default=True,
        ),
    ]
