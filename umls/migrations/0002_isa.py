# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CHILD_CUI', models.CharField(max_length=8, db_index=True)),
                ('PARENT_CUI', models.CharField(max_length=8, db_index=True)),
                ('SAB', models.CharField(max_length=20, db_index=True)),
            ],
            options={
                'db_table': 'ISA',
            },
            bases=(models.Model,),
        ),
    ]
