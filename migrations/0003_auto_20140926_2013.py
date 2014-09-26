# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ARClient', '0002_auto_20140926_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='port',
            field=models.IntegerField(default=b'1818', max_length=5, verbose_name=b'Device port to use for connections'),
        ),
    ]
