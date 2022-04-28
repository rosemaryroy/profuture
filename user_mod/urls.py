from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^login$',views.login,name='login'),
    re_path(r'^register$',views.register,name='register'),
    re_path(r'^logreg$',views.logreg,name='logreg'),
    re_path(r'^home$',views.home,name='home'),
    re_path(r'^studhome$',views.studhome,name='studhome'),
    re_path(r'^clienthome$',views.clienthome,name='clienthome'),
    re_path(r'^loginpage$',views.loginpage,name='loginpage'),
    re_path(r'^mcq$',views.mcq,name='mcq'),
    re_path(r'^tutorial$',views.tutorial,name='tutorial'),
    re_path(r'^project/(?P<id>\d+)$',views.project,name='project'),

]