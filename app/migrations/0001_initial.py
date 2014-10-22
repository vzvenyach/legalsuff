# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sufficiency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', model_utils.fields.StatusField(default=b'draft', max_length=100, no_check_for_status=True, choices=[(b'draft', b'draft'), (b'published', b'published')])),
                ('councilmember', models.CharField(default=b'Chairman Phil Mendelson', max_length=60, choices=[(b'Chairman Phil Mendelson', b'Chairman Phil Mendelson'), (b'Councilmember Yvette Alexander', b'Councilmember Yvette Alexander')])),
                ('measure_type', models.CharField(default=b'Bill', max_length=30, choices=[(b'Bill', b'Bill'), (b'Proposed Resolution', b'Proposed Resolution')])),
                ('measure_number', models.CharField(max_length=15)),
                ('short_title', models.CharField(max_length=100)),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
