# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ARClient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='pubip',
            field=models.CharField(max_length=375, verbose_name=b'Device public IP or hostname', blank=True),
        ),
    ]
