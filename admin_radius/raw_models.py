# This is an auto-generated Django model module.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

RADOP_CHECK_TYPES = (
    (':=', ':='),
    ('==', '=='),
    ('+=', '+='),
    ('!=', '!='),
    ('>', '>'),
    ('>=', '>='),
    ('<', '<'),
    ('<=', '<='),
    ('=~', '=~'),
    ('!~', '!~'),
    ('=*', '=*'),
    ('!*', '!*'),
)

RADOP_REPLY_TYPES = (
    ('=', '='),
    (':=', ':='),
    ('+=', '+='),
)

class Radacct(models.Model):
    radacctid = models.BigIntegerField(primary_key=True)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(unique=True, max_length=32)
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    realm = models.CharField(max_length=64, blank=True)
    nasipaddress = models.GenericIPAddressField()
    nasportid = models.CharField(max_length=15, blank=True)
    nasporttype = models.CharField(max_length=32, blank=True)
    acctstarttime = models.DateTimeField(blank=True, null=True)
    acctupdatetime = models.DateTimeField(blank=True, null=True)
    acctstoptime = models.DateTimeField(blank=True, null=True)
    acctinterval = models.IntegerField(blank=True, null=True)
    acctsessiontime = models.IntegerField(blank=True, null=True)
    acctauthentic = models.CharField(max_length=32, blank=True)
    connectinfo_start = models.CharField(max_length=50, blank=True)
    connectinfo_stop = models.CharField(max_length=50, blank=True)
    acctinputoctets = models.BigIntegerField(blank=True, null=True)
    acctoutputoctets = models.BigIntegerField(blank=True, null=True)
    calledstationid = models.CharField(max_length=50)
    callingstationid = models.CharField(max_length=50)
    acctterminatecause = models.CharField(max_length=32)
    servicetype = models.CharField(max_length=32, blank=True)
    framedprotocol = models.CharField(max_length=32, blank=True)
    framedipaddress = models.GenericIPAddressField()

    class Meta:
        managed = False
        db_table = 'radacct'
        verbose_name_plural = 'radacct'
        
    def __str__(self):
        return "<Radacct {}>".format(self.radacctid)
        

class Radcheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radcheck'
        verbose_name_plural = 'radcheck'
        
    def __str__(self):
        return "<Radcheck {}, {}>".format(self.username, self.value)


class Radgroupcheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radgroupcheck'
        verbose_name_plural = 'radgroupcheck'
        
    def __str__(self):
        return "<Radgroupcheck {}, {}>".format(self.groupname, self.value)
        
        
class Radgroupreply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radgroupreply'
        verbose_name_plural = 'radgroupreply'
        
    def __str__(self):
        return "<Radgroupreply {}, {}>".format(self.groupname, self.value)
        
        
class Radreply(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radreply'
        verbose_name_plural = 'radreply'
        
    def __str__(self):
        return "<Radreply {}, {}>".format(self.username, self.value)


class Radusergroup(models.Model):
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    priority = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'radusergroup'
        verbose_name_plural = 'radusergroup'
        
    def __str__(self):
        return "<Radusergroup {}, {}>".format(self.username, self.groupname)
        

class Radpostauth(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(db_column='pass', max_length=64)  # Field renamed because it was a Python reserved word.
    reply = models.CharField(max_length=32)
    authdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radpostauth'
        verbose_name_plural = 'radpostauth'
        
    def __str__(self):
        return "<Radpostauth {}, {}>".format(self.username, self.authdate)

        
class Nas(models.Model):
    NAS_TYPES = (
        ('ascend', 'ascend'),
        ('bay', 'bay'),
        ('cisco', 'cisco'),
        ('cisco_l2tp', 'cisco_l2tp'),
        ('computone', 'computone'),
        ('cvx', 'cvx'),
        ('digitro', 'digitro'),
        ('dot1x', 'dot1x'),
        ('livingston', 'livingston'),
        ('max40xx', 'max40xx'),
        ('mikrotik', 'mikrotik'),
        ('mikrotik_snmp', 'mikrotik_snmp'),
        ('multitech', 'multitech'),
        ('netserver', 'netserver'),
        ('other', 'other'),
        ('pathras', 'pathras'),
        ('patton', 'patton'),
        ('portslave', 'portslave'),
        ('pr3000', 'pr3000'),
        ('pr4000', 'pr4000'),
        ('redback', 'redback'),
        ('tc', 'tc'),
        ('usrhiper', 'usrhiper'),
        ('versanet', 'versanet'),
    )
    
    nasname = models.CharField(max_length=128)
    shortname = models.CharField(max_length=32, blank=True)
    type = models.CharField(max_length=30, blank=True, choices=NAS_TYPES, default='other')
    ports = models.IntegerField(blank=True, null=True)
    secret = models.CharField(max_length=60)
    server = models.CharField(max_length=64, blank=True)
    community = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'nas'
        verbose_name_plural = 'nas'
        
    def __str__(self):
        return "<Nas {}>".format(self.nasname)
