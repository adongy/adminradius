from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import RadUser, RadPass, RadStartDate, RadEndDate
import hashlib
import datetime

def ntlm_hash(password):
    return hashlib.new('md4', password.encode('utf-16le')).hexdigest()

class DatePickerWidget(forms.DateInput):
    def __init__(self, *args, **kwargs):
        super(DatePickerWidget, self).__init__(*args, **kwargs)
        self.attrs.update({
            'data-provide': 'datepicker',
            'data-date-format': 'dd/mm/yyyy',
        })
        
    class Media:
        #css = {'screen': ('css/datepicker3.css',),}
        #js = ('js/bootstrap-datepicker.js',)
        css = {'screen': ('//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.1/css/datepicker3.min.css',),}
        js = ('//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.1/js/bootstrap-datepicker.min.js',)
    
class RadUserForm(forms.ModelForm):
    username = forms.RegexField(r'^[0-9a-zA-Z\.@\-_]+$', 
                                min_length=3, max_length=20,
                                error_messages={'invalid': _('Only letters, digests and .@-_ are allowed.')})
    class Meta:
        model = RadUser
        fields = ('username',)
        
class RadStartDateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RadStartDateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            try:
                self.initial['value'] = datetime.datetime.strptime(self.initial.get('value'), '%Y%m%d').strftime('%d/%m/%Y')
            except ValueError:
                pass
                
    # Enforce field type to get date validations
    value = forms.DateField(label=_("Start Date"), input_formats=('%d/%m/%Y', '%d/%m/%y',),
                            widget=DatePickerWidget())
    
    def clean_value(self):
        # We get a datetime.date object
        value = self.cleaned_data.get('value')
        
        return value.strftime('%Y%m%d')
    
    class Meta:
        model = RadStartDate
        fields = ('value',)
        
class RadEndDateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RadEndDateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            try:
                self.initial['value'] = datetime.datetime.strptime(self.initial.get('value'), '%Y%m%d').strftime('%d/%m/%Y')
            except ValueError:
                pass

    # Enforce field type to get date validations
    value = forms.DateField(label=_("End Date"), input_formats=('%d/%m/%Y', '%d/%m/%y',),
                            widget=DatePickerWidget())
    
    def clean_value(self):
        # We get a datetime.date object
        value = self.cleaned_data.get('value')
        
        return value.strftime('%Y%m%d')
        
    class Meta:
        model = RadEndDate
        fields = ('value',)
        
class RadPassForm(forms.ModelForm):

    value = forms.CharField(label=_("Password"), required=False, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label=_("Confirm Password"), required=False, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RadPassForm, self).clean()
        password1 = cleaned_data.get('value')
        password2 = cleaned_data.get('confirm_password')
        
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_("The two password fields didn't match."))
    
    def clean_value(self):
        data = self.cleaned_data.get('value')
        
        if data:
            return ntlm_hash(data)
        else:
            return data
            
    def clean_confirm_password(self):
        data = self.cleaned_data.get('confirm_password')
        
        if data:
            return ntlm_hash(data)
        else:
            return data
            
        
    class Meta:
        model = RadPass
        fields = ('value',)