from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .models import *
from admin_mod.models import *

# Create your views here.
def index(request):
    return render(request,'user_mod/index.html')
def logreg(request):
    return render(request,'user_mod/logreg.html')
def loginpage(request):
    return render(request,'user_mod/logreg.html')

def login(request):
    if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)
      if user is not None:
        auth.login(request,user)
        cur_user=request.user
        user_id=cur_user.id
        

        usert= userprofile.objects.get(userid_id=user_id)
        print(usert.usertype)
        if usert.usertype=='Student':
            messages.info(request,'login successfully')
            return redirect('studhome')
        if usert.usertype=='Client':
            messages.info(request,'login successfully')
            return redirect('clienthome')
        else:
            return redirect('loginpage')
      
    
       
    return redirect('loginpage')

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
    plat = platform.objects.filter(userid_id=request.user)
    
    plat2 = platform.objects.all()
    proj = project_table.objects.all()
    return render(request,'user_mod/clienthome.html',{'plat': plat, 'proj':proj, 'plat2':plat2})

def project(request, id):
    iproject = project_table.objects.get(projectid=id)
    return render(request,'user_mod/project.html', {'iproject': iproject})

def mcq(request):
    multiple = course_mcq.object.all()
    return render(request,'user_mod/mcq.html',{'multiple':multiple})