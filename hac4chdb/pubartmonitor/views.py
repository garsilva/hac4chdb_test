from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import auth


def isLoggedIn(request, un):
    if not request.user.is_authenticated or not request.user.username==un:
        return False
    return True

def username_exists(un):
    if User.objects.filter(username=un).exists():
        return True
    return False

def email_exists(em):
    if User.objects.filter(email=em).exists():
        return True
    return False

def index(request):
    template = loader.get_template('pubartmonitor/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('pubartmonitor/signup.html')
    context = {}

    success = True
    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        p1 = request.POST['password']
        p2 = request.POST['cpassword']
        if p1 != p2:
            messages.error(request, "passwords don't match")
            context = {'error': "passwords don't match, try again"}
            success = False

        if username_exists(username):
            messages.error(request, "username already in db")
            context = {'error': "username already in db, try again"}
            success = False

        if email_exists(email):
            messages.error(request, "email already in db")
            context = {'error': "email already in db, try again"}
            success = False

        if success:
            myuser = User.objects.create_user(username, email, p1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been created")
            template = loader.get_template('pubartmonitor/signin.html')
            context = {'un': username}

    return HttpResponse(template.render(context, request))


def signin(request):
    template = loader.get_template('pubartmonitor/signin.html')
    context = {'error': '', 'un':''}
    success = False
    un = ''
    if request.method=="POST":
        un = request.POST['username']
        p1 = request.POST['password']

        user = authenticate(username=un, password = p1)
        if user is not None:
            login(request, user)
            success = True
        else:
            messages.error(request, "bad credentials")
            context = {'error': "username or password invalid, try again"}
            success = False
    if success:
        context = {'user': un}
        template = loader.get_template('pubartmonitor/publichomeredirect.html')

    return HttpResponse(template.render(context, request))

def signout(request):
    template = loader.get_template('pubartmonitor/signout.html')
    context = {'user': request.user}

    if request.method=='POST':
        value = request.POST['bt']
        if value == "yes":
            if request.user.is_authenticated:
                auth.logout(request)
                template = loader.get_template('pubartmonitor/index.html')
                context = {}
        else:
            template = loader.get_template('pubartmonitor/publichomeredirect.html')
            context = {'user': request.user.username}
    return HttpResponse(template.render(context, request))


def publichome(request, username):
    if not isLoggedIn(request, username):
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    template = loader.get_template('pubartmonitor/publichome.html')
    context = {'user':username}
    return HttpResponse(template.render(context, request))
