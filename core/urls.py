from django.conf.urls.defaults import *
from django.contrib.auth.models import User

urlpatterns = patterns('',
    (r'^$','auth_test.core.views.index'),
    (r'^users/$','django.views.generic.list_detail.object_list',{'queryset': User.objects.all()}),
    (r'^registration/$','django.views.generic.simple.direct_to_template',{'template':'registration.html'}),
    (r'^register/$','auth_test.core.views.register'),
    (r'^login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^logout/$','django.contrib.auth.views.logout',{'template_name':'logged_out.html'}),
)
