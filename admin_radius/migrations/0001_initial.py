# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nasname', models.CharField(max_length=128)),
                ('shortname', models.CharField(max_length=32, blank=True)),
                ('type', models.CharField(default='other', max_length=30, blank=True, choices=[('ascend', 'ascend'), ('bay', 'bay'), ('cisco', 'cisco'), ('cisco_l2tp', 'cisco_l2tp'), ('computone', 'computone'), ('cvx', 'cvx'), ('digitro', 'digitro'), ('dot1x', 'dot1x'), ('livingston', 'livingston'), ('max40xx', 'max40xx'), ('mikrotik', 'mikrotik'), ('mikrotik_snmp', 'mikrotik_snmp'), ('multitech', 'multitech'), ('netserver', 'netserver'), ('other', 'other'), ('pathras', 'pathras'), ('patton', 'patton'), ('portslave', 'portslave'), ('pr3000', 'pr3000'), ('pr4000', 'pr4000'), ('redback', 'redback'), ('tc', 'tc'), ('usrhiper', 'usrhiper'), ('versanet', 'versanet')])),
                ('ports', models.IntegerField(null=True, blank=True)),
                ('secret', models.CharField(max_length=60)),
                ('server', models.CharField(max_length=64, blank=True)),
                ('community', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'db_table': 'nas',
                'managed': False,
                'verbose_name_plural': 'nas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radacct',
            fields=[
                ('radacctid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('acctsessionid', models.CharField(max_length=64)),
                ('acctuniqueid', models.CharField(unique=True, max_length=32)),
                ('username', models.CharField(max_length=64)),
                ('groupname', models.CharField(max_length=64)),
                ('realm', models.CharField(max_length=64, blank=True)),
                ('nasipaddress', models.GenericIPAddressField()),
                ('nasportid', models.CharField(max_length=15, blank=True)),
                ('nasporttype', models.CharField(max_length=32, blank=True)),
                ('acctstarttime', models.DateTimeField(null=True, blank=True)),
                ('acctupdatetime', models.DateTimeField(null=True, blank=True)),
                ('acctstoptime', models.DateTimeField(null=True, blank=True)),
                ('acctinterval', models.IntegerField(null=True, blank=True)),
                ('acctsessiontime', models.IntegerField(null=True, blank=True)),
                ('acctauthentic', models.CharField(max_length=32, blank=True)),
                ('connectinfo_start', models.CharField(max_length=50, blank=True)),
                ('connectinfo_stop', models.CharField(max_length=50, blank=True)),
                ('acctinputoctets', models.BigIntegerField(null=True, blank=True)),
                ('acctoutputoctets', models.BigIntegerField(null=True, blank=True)),
                ('calledstationid', models.CharField(max_length=50)),
                ('callingstationid', models.CharField(max_length=50)),
                ('acctterminatecause', models.CharField(max_length=32)),
                ('servicetype', models.CharField(max_length=32, blank=True)),
                ('framedprotocol', models.CharField(max_length=32, blank=True)),
                ('framedipaddress', models.GenericIPAddressField()),
            ],
            options={
                'db_table': 'radacct',
                'managed': False,
                'verbose_name_plural': 'radacct',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radcheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(max_length=2, choices=[('=', '='), (':=', ':='), ('+=', '+=')])),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radcheck',
                'managed': False,
                'verbose_name_plural': 'radcheck',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radgroupcheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(max_length=2, choices=[('=', '='), (':=', ':='), ('+=', '+=')])),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radgroupcheck',
                'managed': False,
                'verbose_name_plural': 'radgroupcheck',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radgroupreply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(max_length=2, choices=[('=', '='), (':=', ':='), ('+=', '+=')])),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radgroupreply',
                'managed': False,
                'verbose_name_plural': 'radgroupreply',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radpostauth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64, db_column='pass')),
                ('reply', models.CharField(max_length=32)),
                ('authdate', models.DateTimeField()),
            ],
            options={
                'db_table': 'radpostauth',
                'managed': False,
                'verbose_name_plural': 'radpostauth',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radreply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(max_length=2, choices=[('=', '='), (':=', ':='), ('+=', '+=')])),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radreply',
                'managed': False,
                'verbose_name_plural': 'radreply',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radusergroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('groupname', models.CharField(max_length=64)),
                ('priority', models.IntegerField()),
            ],
            options={
                'db_table': 'radusergroup',
                'managed': False,
                'verbose_name_plural': 'radusergroup',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RadUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RadEndDate',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('admin_radius.radcheck',),
        ),
        migrations.AddField(
            model_name='raduser',
            name='end_date',
            field=models.OneToOneField(to='admin_radius.RadEndDate'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='RadPass',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('admin_radius.radcheck',),
        ),
        migrations.AddField(
            model_name='raduser',
            name='password',
            field=models.OneToOneField(null=True, blank=True, to='admin_radius.RadPass'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='RadStartDate',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('admin_radius.radcheck',),
        ),
        migrations.AddField(
            model_name='raduser',
            name='start_date',
            field=models.OneToOneField(to='admin_radius.RadStartDate'),
            preserve_default=True,
        ),
        migrations.RunSQL(
            sql='ALTER TABLE radusergroup ADD id INT(11) NOT NULL auto_increment PRIMARY KEY FIRST;',
            reverse_sql='ALTER TABLE radusergroup DROP id;',
        ),
    ]
