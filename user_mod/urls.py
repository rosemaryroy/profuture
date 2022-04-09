from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logreg',views.logreg,name='logreg'),
    path('home',views.home,name='home'),
    path('studhome',views.studhome,name='studhome'),
    path('clienthome',views.clienthome,name='clienthome'),

]