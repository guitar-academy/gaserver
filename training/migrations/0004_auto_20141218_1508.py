# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_auto_20141218_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warmup',
            old_name='entries',
            new_name='songs',
        ),
    ]
