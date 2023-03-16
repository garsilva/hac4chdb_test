from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('pubartmonitor/index', views.index, name='index'),
    path('pubartmonitor/signup', views.signup, name='signup'),
    path('pubartmonitor/signin', views.signin, name='signin'),
    path('pubartmonitor/signout', views.signout, name='signout'),
    path('pubartmonitor/publichome/<str:username>', views.publichome, name='public home'),
    #path('pubartmonitor/publichomeredirect', views.publichomeredirect, name='publichomeredirect')
]
