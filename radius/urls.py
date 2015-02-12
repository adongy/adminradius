from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings

admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER
admin.site.index_title = settings.INDEX_TITLE

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(pattern_name='admin_radius:home')),
    url(r'^manage/', include('admin_radius.urls', namespace='admin_radius')),
    url(r'^admin/', include(admin.site.urls)),
)