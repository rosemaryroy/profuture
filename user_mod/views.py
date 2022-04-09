from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .models import *

# Create your views here.
def index(request):
    return render(request,'user_mod/index.html')
def logreg(request):
    return render(request,'user_mod/logreg.html')



def login(request) :
    if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password) 
      if user is not None:
        auth.login(request,user)
        messages.info(request,'login successfully')
        return redirect('clienthome')


def register(request):
    #try:
        if request.method =='POST':
           firstname = request.POST['first_name']
           lastname = request.POST['last_name']
           username = request.POST['username']
           email = request.POST['email']
           password = request.POST['password']
           usertype = request.POST['usertype']
           user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
           user.save()
        #    user1 = User.objects.get(username=username)
           user_profile=userprofile(usertype=usertype,userid=user)
           user_profile.save()
           return redirect('logreg')
        #else: 
            #return redirect('login')
    #except:
         #return redirect('login')
def home(request):
    return render(request,'user_mod/home.html')
def studhome(request):
    return render(request,'user_mod/studhome.html')
def clienthome(request):
    #plat=platform.objects.all()

    #proj=project.objects.all()
    plat = platform.objects.filter(userid=request.user)
    return render(request,'user_mod/clienthome.html',{'platform': plat})