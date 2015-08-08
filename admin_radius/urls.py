from django.conf.urls import patterns, url, include

from .views import home, user_detail, user_list, acct_detail

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^user/', include(patterns('',
        url(r'^$', user_list, name='user_list'),
        url(r'^add/$', user_detail, name='user_add'),
        url(r'^edit/(?P<username>[\w.-_]+)/$', user_detail, name='user_edit'),
        url(r'^delete/(?P<username>[\w.-_]+)/$', user_delete, name='user_delete'),
    ))),
    url(r'^acct/', include(patterns('',
        url(r'^user/(?P<username>[\w.-_]+)/(?P<format>\w*)/$', acct_detail, name='user_acct'),
        url(r'^(?P<format>\w*)/$', acct_detail, name='total_acct'),
    ))),
)