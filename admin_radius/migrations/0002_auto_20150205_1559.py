# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def loadfixture(apps, schema_editor):
    call_command('loaddata', 'radcheck.json')
    call_command('loaddata', 'raduser.json')


class Migration(migrations.Migration):

    dependencies = [
        ('admin_radius', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadfixture),
    ]
