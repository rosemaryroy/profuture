from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('login_page',views.login_page,name='login_page'),
    path('login',views.login,name='login'),
    path('register_page',views.register_page,name='register_page'),
    path('register',views.register,name='register'),
    path('base_ext',views.base_ext,name='base_ext'),
    path('add_project_show',views.add_project_show,name='add_project_show'),
    path('add_pro_edit',views.add_pro_edit,name='add_pro_edit'),
    
]
    
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
