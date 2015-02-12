from django.db import models
from .raw_models import *
from django.core.urlresolvers import reverse
import datetime
from django.core.exceptions import ValidationError
    
class RadPassManager(models.Manager):
    def get_queryset(self):
        return super(RadPassManager, self).get_queryset().filter(attribute='NT-Password', op=':=')

class RadStartDateManager(models.Manager):
    def get_queryset(self):
        return super(RadStartDateManager, self).get_queryset().filter(attribute='User-Start-Date', op=':=')

class RadEndDateManager(models.Manager):
    def get_queryset(self):
        return super(RadEndDateManager, self).get_queryset().filter(attribute='User-End-Date', op=':=')

class RadPass(Radcheck):
    objects = RadPassManager()
    
    def __init__(self, *args, **kwargs):
        self._meta.get_field('attribute').default = 'NT-Password'
        self._meta.get_field('op').default = ':='
        super(RadPass, self).__init__(*args, **kwargs)
    
    def clean_fields(self, exclude=None):
        super(RadPass, self).clean_fields(exclude)
        if self.value and len(self.value) != 32:
            raise ValidationError(_("Hash is incorrectly formatted. Input as a 32 hexadecimal character string without a leading '0x' prefix."))
        
    class Meta:
        proxy = True
        
class RadStartDate(Radcheck):
    objects = RadStartDateManager()
    
    def __init__(self, *args, **kwargs):
        self._meta.get_field('attribute').default = 'User-Start-Date'
        self._meta.get_field('op').default = ':='
        super(RadStartDate, self).__init__(*args, **kwargs)
        
    def clean_fields(self, exclude=None):
        super(RadStartDate, self).clean_fields(exclude)
        if self.value:
            try:
                datetime.datetime.strptime(self.value, '%Y%m%d')
            except ValueError:
                raise ValidationError(_("Input date is not formatted as YYYYMMDD."))
            
    def get_date(self):
        if self.value:
            return datetime.datetime.strptime(self.value, '%Y%m%d')
        else:
            return None
    
    def get_absolute_url(self):
        return reverse('admin_radius:user_edit', args=(self.username,))
                
    class Meta:
        proxy = True
        
class RadEndDate(Radcheck):
    objects = RadEndDateManager()
    
    def __init__(self, *args, **kwargs):
        self._meta.get_field('attribute').default = 'User-End-Date'
        self._meta.get_field('op').default = ':='
        super(RadEndDate, self).__init__(*args, **kwargs)
        
    def clean_fields(self, exclude=None):
        super(RadEndDate, self).clean_fields(exclude)
        if self.value:
            try:
                datetime.datetime.strptime(self.value, '%Y%m%d')
            except ValueError:
                raise ValidationError(_("Input date is not formatted as YYYYMMDD."))
            
    def get_date(self):
        if self.value:
            return datetime.datetime.strptime(self.value, '%Y%m%d')
        else:
            return None
    
    def get_absolute_url(self):
        return reverse('admin_radius:user_edit', args=(self.username,))
                
    class Meta:
        proxy = True
        
class RadUser(models.Model):
    username = models.CharField(max_length=64, unique=True)
    start_date = models.OneToOneField(RadStartDate)
    end_date = models.OneToOneField(RadEndDate)
    password = models.OneToOneField(RadPass, blank=True, null=True)
    
    @property
    def is_online(self):
        return Radacct.objects.filter(
            username=self.username,
            acctstoptime=None).exists()
            
    def clean(self):
        # username must be consistent
        if self.start_date and self.username and self.start_date.username != self.username:
            raise ValidationError({'start_date': _('Usernames do not match.')})
        if self.end_date and self.username and self.end_date.username != self.username:
            raise ValidationError({'end_date': _('Usernames do not match.')})
        if self.password and self.username and self.password.username != self.username:
            raise ValidationError({'password': _('Usernames do not match.')})
    
    def get_absolute_url(self):
        return reverse('admin_radius:user_edit', args=(self.username,))
        
    def __str__(self):
        return "<Raduser {}>".format(self.username)