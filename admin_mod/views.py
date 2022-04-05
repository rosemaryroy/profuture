from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

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
    plat = platform.objects.filter(userid=request.user)
    return render(request,'admin_mod/add_pro_form.html', {'platform': plat})

def add_pro(request):
    if request.method == 'POST':
        project_name=request.POST['project_name']
        documentation=request.POST['documentation']
        project=request.FILES['project']
        platid = request.POST['platfid']
        plat = platform.objects.get(platformid=platid)
        projects_=project_table(project_name=project_name,documentation=documentation,platformid=plat,project=project)
        projects_.save()
        return redirect('add_project_show')

def add_project_show(request):
    print(request.user.username)
    show=project_table.objects.all()
    return render(request,'admin_mod/add_project_show.html',{'project_table' : show})

def add_pro_edit(request,projectid):
    show=project_table.objects.get(projectid=projectid)
    return render(request,'admin_mod/add_pro_edit.html',{'project_table' : show})

def update(request,projectid):
    projects_=project_table.objects.get(projectid=projectid)
    projects_.project_name=request.POST.get('project_name')
    projects_.documentation=request.POST.get('documentation')
    projects_.save()
    return redirect('add_project_show')

def add_platform_show(request):
    platformshow=platform.objects.all()
    return render(request,'admin_mod/add_platform_show.html',{'platform' : platformshow})

def add_platform_form(request):
    return render(request,'admin_mod/add_platform_form.html')


def add_platform(request):
    if request.method == 'POST':
        platform_name=request.POST['platform_name']
        description=request.POST['description']
        image=request.FILES['image']

        platform_=platform(platform_name=platform_name,description=description,userid=request.user,image=image)
        platform_.save()
        return redirect('add_platform_show')


def add_platform_edit(request, platformid):
    show=platform.objects.get(platformid=platformid)
    return render(request,'admin_mod/add_platform_edit.html',{'platform' : show})

def platform_update(request,platformid):
    platform_=platform.objects.get(platformid=platformid)
    platform_.platform_name=request.POST.get('platform_name')
    platform_.description=request.POST.get('description')
    try:
        platform_.image=request.FILES['image']
    except:
        pass
    platform_.save()
    return redirect('add_platform_show')

def project_delete(request,projectid):
    pro=project_table.objects.get(projectid=projectid)
    pro.delete()
    return redirect('add_project_show')

def platform_delete(request,platformid):
    plat=platform.objects.get(platformid=platformid)
    plat.delete()
    return redirect('add_platform_show')

def project_view(request):
    projectview=project_table.objects.all()
    return render(request,'admin_mod/project_view.html',{'project_table' : projectview})

def add_mcq(request):
    mcqshow=mcq.objects.all()
    return render(request,'admin_mod/add_mcq.html',{'mcq' : mcqshow})

def add_mcq_form(request):
    plat = platform.objects.filter(userid=request.user)
    return render(request,'admin_mod/add_mcq_form.html', {'platform': plat})

def mcq_form(request):
    if request.method == 'POST':
        question=request.POST['question']
        answer=request.POST['answer']
        option1=request.POST['option1']
        option2=request.POST['option2']
        option3=request.POST['option3']
        option4=request.POST['option4']
        platid = request.POST['platfid']
        plat = platform.objects.get(platformid=platid)
        mcq_=mcq(question=question,answer=answer,option1=option1,option2=option2,option3=option3,option4=option4,platformid=plat)
        mcq_.save()
        return redirect('add_mcq')

def add_mcq_edit(request, mcqid):
    show=mcq.objects.get(mcqid=mcqid)
    return render(request,'admin_mod/add_mcq_edit.html',{'mcq' : show})

def mcq_update(request,mcqid):
    mcq_=mcq.objects.get(mcqid=mcqid)
    mcq_.question=request.POST.get('question')
    mcq_.answer=request.POST.get('answer')
    mcq_.option1=request.POST.get('option1')
    mcq_.option2=request.POST.get('option2')
    mcq_.option3=request.POST.get('option3')
    mcq_.option4=request.POST.get('option4')
    
    mcq_.save()
    return redirect('add_mcq')

def mcq_delete(request,mcqid):
    mcq_=mcq.objects.get(mcqid=mcqid)
    mcq_.delete()
    return redirect('add_mcq')