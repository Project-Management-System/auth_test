from django.conf.urls.defaults import *
from django.contrib.auth.models import User
info={'queryset': User.objects.all()}

#profile = {
#           'template_name':'profile.html'
#           }
index = {
         'template':'index.html'
         }
urlpatterns = patterns('',
    (r'^$','django.views.generic.simple.direct_to_template',index),
    (r'^users/$','django.views.generic.list_detail.object_list',info),
    (r'^register/$','auth_test.core.views.register'),
    (r'^login/$','django.contrib.auth.views.login'),
    (r'^logout/$','django.contrib.auth.views.logout',index),
    (r'^user/(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail',info),
#    (r'^profile/$','django.views.generic.simple.direct_to_template',profile),
#    (r'profile/save/$','auth_test.core.views.update_profile'),
)
