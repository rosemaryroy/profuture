from django.shortcuts import redirect

def admin_mod(request):
    return redirect('/admin_mod/')

def user_mod(request):
    return redirect('/user_mod/')