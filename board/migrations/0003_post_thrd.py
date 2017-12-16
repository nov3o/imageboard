# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_remove_post_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thrd',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
