# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MRCONSO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CUI', models.CharField(max_length=8)),
                ('STR', models.TextField()),
                ('CODE', models.CharField(max_length=50)),
                ('LAT', models.CharField(max_length=3)),
                ('ISPREF', models.CharField(max_length=1)),
                ('SAB', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'MRCONSO',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MRREL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CUI1', models.CharField(max_length=8)),
                ('REL', models.CharField(max_length=2)),
                ('RELA', models.CharField(max_length=100)),
                ('CUI2', models.CharField(max_length=8)),
                ('SAB', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'MRREL',
            },
            bases=(models.Model,),
        ),
    ]
