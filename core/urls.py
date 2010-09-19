from django.conf.urls.defaults import *
from django.contrib.auth.models import User
info={'queryset': User.objects.all()}
urlpatterns = patterns('',
    (r'^$','auth_test.core.views.index'),
    (r'^users/$','django.views.generic.list_detail.object_list',info),
    (r'^registration/$','django.views.generic.simple.direct_to_template',{'template':'registration.html'}),
    (r'^register/$','auth_test.core.views.register'),
    (r'^login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^logout/$','django.contrib.auth.views.logout',{'template_name':'logged_out.html'}),
    (r'^user/(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail',info),
)
