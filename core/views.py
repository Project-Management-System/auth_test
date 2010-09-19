from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from auth_test.core.forms import Registration_form

def register(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    mail = request.POST.get('email','')
    if username and password and mail:
        try:
            User.objects.create_user(username, mail, password)
        except:
            return render_to_response('registration/register.html',{'error':'Username already exist'},context_instance=RequestContext(request))
        return HttpResponseRedirect('/core/login/')
    return render_to_response('registration/register.html', {'form': Registration_form()},context_instance=RequestContext(request))

def update_profile():
    pass