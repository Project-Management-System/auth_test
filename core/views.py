from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user
from django.shortcuts import render_to_response

def registration(request):
    user = get_user(request)
    render_to_response('registration.help',locals())

def register(request):
    username = request.POST['login']
    password = request.POST['password']
    mail = request.POST['mail']
    try:
        User.objects.create_user(username, mail, password)
    except:
        #return render_to_response('registration.html',{'error':'Username already exist'})
        return HttpResponseRedirect('/core/registration/',{'error':'Username already exist'})
    return HttpResponseRedirect('/core/users/')

def index(request):
    user = get_user(request)
    return render_to_response('index.html',locals())