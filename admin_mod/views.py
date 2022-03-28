from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


from admin_mod.models import admin_reg


# Create your views here.
def index(request):
    return render(request,'admin_mod/index.html')

def login_page(request):
    return render(request,'admin_mod/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        messages.info(request, 'login successfully')
        if user is not None:
            auth.login(request,user)
            return redirect('base_ext')
        else:
            return redirect('base_ext')
def register_page(request):
    return render(request,'admin_mod/register.html')

def register(request):
    #try:
        if request.method == 'POST':
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            confirm_pswd = request.POST['cnfm_password']
            user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
            user.save()
            return redirect('login_page')
        #else:
            #return redirect('login')
    #except:
        #return redirect('login')

def base_ext(request):
    return render(request,'admin_mod/base_ext.html')

def add_project_show(request):
    show=project.objects.all()
    return render(request,'admin_mod/add_project_show.html',{'project' : show})

def add_pro_edit(request):
    show=project.objects.get(projectid=project)
    return render(request,'admin_mod/add_pro_edit.html',{'student_profile' : show})