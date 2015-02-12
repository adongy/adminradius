from django.conf import settings
from django.contrib import admin

from .models import Radacct, Radcheck, Radgroupcheck, Radgroupreply, Radreply, Radusergroup, Radpostauth, Nas
from .models import RadUser

class RadpostauthAdmin(admin.ModelAdmin):
    list_display   = ('username', 'reply', 'authdate',)
    list_filter    = ('username', 'reply',)
    
class RadreplyAdmin(admin.ModelAdmin):
    list_display   = ('username', 'attribute', 'op', 'value',)
    list_filter    = ('username',)
    search_fields  = ('attribute', 'value',)

class RadusergroupAdmin(admin.ModelAdmin):
    list_display   = ('groupname', 'username',)
    list_filter    = ('groupname',)
    search_fields  = ('username',)

class RadcheckAdmin(admin.ModelAdmin):
    list_display   = ('username', 'attribute', 'op', 'value',)
    list_filter    = ('username',)
    search_fields  = ('attribute', 'value',)

class RadgroupcheckAdmin(admin.ModelAdmin):
    list_display   = ('groupname', 'attribute', 'op', 'value',)
    list_filter    = ('groupname',)

class RadgroupreplyAdmin(admin.ModelAdmin):
    list_display   = ('groupname', 'attribute', 'op', 'value',)
    list_filter    = ('groupname',)

class RadacctAdmin(admin.ModelAdmin):
    list_display   = ('acctuniqueid', 'username', 'nasipaddress', 'acctstarttime', 'acctsessiontime',)
    list_filter    = ('nasipaddress',)

class NasAdmin(admin.ModelAdmin):
    list_display   = ('nasname', 'shortname', 'type', 'ports', 'secret', 'community',)
    list_filter    = ('type', 'community',)
    ordering       = ('nasname',)
    search_fields  = ('nasname', 'shortname', 'ports', 'community',)

class RadUserAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Radpostauth, RadpostauthAdmin)
admin.site.register(Radreply,RadreplyAdmin)
admin.site.register(Radusergroup,RadusergroupAdmin)
admin.site.register(Radcheck,RadcheckAdmin)
admin.site.register(Radgroupcheck,RadgroupcheckAdmin)
admin.site.register(Radgroupreply,RadgroupreplyAdmin)
admin.site.register(Radacct,RadacctAdmin)
admin.site.register(Nas,NasAdmin)
admin.site.register(RadUser, RadUserAdmin)