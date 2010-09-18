from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def register(request):
    username = request.POST['login']
    password = request.POST['password']
    mail = request.POST['mail']
    User.objects.create_user(username, mail, password)
    return HttpResponseRedirect('/core/users/')