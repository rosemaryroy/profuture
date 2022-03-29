from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *





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


def add_pro_form(request):
    return render(request,'admin_mod/add_pro_form.html')

def add_pro(request):
    if request.method == 'POST':
        project_name=request.POST['project_name']
        documentation=request.POST['documentation']
        project=request.FILES['project']

        projects_=project_table(project_name=project_name,documentation=documentation)
        projects_.save()
        platform_=platform(platformid=projects_,project=project)
        platform_.save()
        return redirect('add_project_show')

def add_project_show(request):
    print(request.user.username)
    show=project_table.objects.all()
    return render(request,'admin_mod/add_project_show.html',{'project_table' : show})

def add_pro_edit(request):
    show=project_table.objects.get(projectid=project_table)
    return render(request,'admin_mod/add_pro_edit.html',{'project_table' : show})

def update(request,platformid):
    projects_=project_table.objects.get(platformid=platformid)
    project_table.project_name=request.POST.get('project_name')
    project_table.documentation=request.POST.get('documentation')
    projects_.save()
    platform_=platform.objects.get(platformid=projects_)
    platform_.save()
    return redirect('add_project_show')

def add_platform_show(request):
    show=platform.objects.all()
    return render(request,'admin_mod/add_platform_show.html',{'platform' : show})

def add_platform_form(request):
    return render(request,'admin_mod/add_platform_form.html')


def add_platform(request):
    if request.method == 'POST':
        platform_name=request.POST['platform_name']
        description=request.POST['description']
        image=request.FILES['image']

        platform_=platform(platform_name=platform_name,description=description)
        platform_.save()
        project_=project_table(userid=platform_,image=image)
        project_.save()
        return redirect('add_platform_show')


def add_platform_edit(request):
    show=platform.objects.get(platformid=platform)
    return render(request,'admin_mod/add_platform_edit.html',{'platform' : show})

def platform_update(request,userid):
    platform_=platform.objects.get(userid=userid)
    platform.platform_name=request.POST.get('platform_name')
    platform.description=request.POST.get('description')
    platform_.save()
    project_=project_table.objects.get(platformid=platform_)
    project_.save()
    return redirect('add_platform_show')
