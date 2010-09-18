from django.conf.urls.defaults import *
from django.contrib.auth.models import User

urlpatterns = patterns('',
    (r'^$','django.views.generic.simple.direct_to_template',{'template':'index.html'}),
    (r'^users/$','django.views.generic.list_detail.object_list',{'queryset': User.objects.all()}),
    (r'^registration/$','django.views.generic.simple.direct_to_template',{'template':'registration.html'}),
    (r'^register/$','auth_test.core.views.register'),
)
