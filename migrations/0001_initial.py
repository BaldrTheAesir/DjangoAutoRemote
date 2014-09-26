# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(max_length=15, serialize=False, verbose_name=b'Device ID', primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Device Name')),
                ('LANip', models.GenericIPAddressField(protocol=b'IPv4', verbose_name=b'Device LAN IP')),
                ('pubip', models.CharField(max_length=375, verbose_name=b'Device public IP or hostname')),
                ('port', models.IntegerField(max_length=5, null=True, verbose_name=b'Device port to use for connections')),
                ('ttl', models.IntegerField(default=0, max_length=15, verbose_name=b'Message TTL')),
                ('gcm_key', models.CharField(max_length=4096, verbose_name=b'Device GCM key (if available)', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'AutoRemote Device',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(max_length=15, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name=b'Type handle')),
                ('desc', models.CharField(max_length=750, verbose_name=b'Type description')),
                ('has_wifi', models.BooleanField(default=True, verbose_name=b'WiFI enabled?')),
                ('icon_url', models.URLField(max_length=650)),
                ('can_rec_files', models.NullBooleanField(default=False)),
                ('default_port', models.IntegerField(default=None, null=True)),
                ('gcm', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Device type',
                'verbose_name_plural': 'Device types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.ForeignKey(to='ARClient.Type'),
            preserve_default=True,
        ),
    ]
