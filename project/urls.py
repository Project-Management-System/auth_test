from django.conf.urls.defaults import *

index = {
         'template':'projects.html',
         }

urlpatterns = patterns('',
    (r'^myprojects/$','django.views.generic.simple.direct_to_template',index),
    (r'newproject/$','auth_test.project.views.creat_project')
)
