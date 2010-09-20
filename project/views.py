from auth_test.project.models import Project
from django.shortcuts import render_to_response
from auth_test.project.forms import Creat_project_form
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
import datetime

#def myprojects(request):
#    user = get_user(request)
#    return render_to
def creat_project(request):
    name=request.POST.get('name','')
    description=request.POST.get('description','')
    license=request.POST.get('license','')
    site=request.POST.get('site','')
    if name and description and license and site:
        print request.user.birthday
        Project(name=name,description=description,date_started=datetime.datetime.now(),
                web_site=site,license=license, super_admin=request.user).save()
        return HttpResponseRedirect('/projects/')        
    form = Creat_project_form()
    return render_to_response('creat_project.html',locals(),context_instance=RequestContext(request))
    