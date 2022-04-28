from django.contrib import admin
from django.urls import re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^login_page$',views.login_page,name='login_page'),
    re_path(r'^ad_login$',views.ad_login,name='ad_login'),
    re_path(r'^register_page$',views.register_page,name='register_page'),
    re_path(r'^register$',views.register,name='register'),
    re_path(r'^base_ext$',views.base_ext,name='base_ext'),
    re_path(r'^add_pro_form$',views.add_pro_form,name='add_pro_form'),
    re_path(r'^add_pro$',views.add_pro,name='add_pro'),
    re_path(r'^add_project_show$',views.add_project_show,name='add_project_show'),
    re_path(r'^edit/(?P<projectid>\d+)/$',views.add_pro_edit,name='add_pro_edit'),
    re_path(r'^update/(?P<projectid>\d+)$',views.update,name='update'),
    re_path(r'^add_platform_show$',views.add_platform_show,name='add_platform_show'),
    re_path(r'^add_platform_form$',views.add_platform_form,name='add_platform_form'),
    re_path(r'^add_platform$',views.add_platform,name='add_platform'),
    re_path(r'^platformedit/(?P<platformid>\d+)/$',views.add_platform_edit,name='add_platform_edit'),
    re_path(r'^platformupdate/(?P<platformid>\d+)$',views.platform_update,name='platform_update'),
    re_path(r'^project_delete/(?P<projectid>\d+)/$',views.project_delete,name='project_delete'),
    re_path(r'^platform_delete/(?P<platformid>\d+)/$',views.platform_delete,name='platform_delete'),
    re_path(r'^project_view$',views.project_view,name='project_view'),
    re_path(r'^add_mcq$',views.add_mcq,name='add_mcq'),
    re_path(r'^add_mcq_form$',views.add_mcq_form,name='add_mcq_form'),
    re_path(r'^mcq_form$',views.mcq_form,name='mcq_form'),
    re_path(r'^mcqedit/(?P<mcqid>\d+)/$',views.add_mcq_edit,name='add_mcq_edit'),
    re_path(r'^mcqupdate/(?P<mcqid>\d+)$',views.mcq_update,name='mcq_update'),
    re_path(r'^mcq_delete/(?P<mcqid>\d+)/$',views.mcq_delete,name='mcq_delete'),
    re_path(r'^course$',views.course,name='course'),
    re_path(r'^add_course$',views.add_course,name='add_course'),
    re_path(r'^add_course_form$',views.add_course_form,name='add_course_form'),
    re_path(r'^course_show$',views.course_show,name='course_show'),
    re_path(r'^course_edit/(?P<courseid>\d+)/$',views.course_edit,name='course_edit'),
    re_path(r'^course_update/(?P<courseid>\d+)$',views.course_update,name='course_update'),
    re_path(r'^course_delete/(?P<courseid>\d+)/$',views.course_delete,name='course_delete'),
    re_path(r'^tutorial_video$',views.tutorial_video,name='tutorial_video'),
    re_path(r'^tutorial_video_form$',views.tutorial_video_form,name='tutorial_video_form'),
    re_path(r'^course_mcq$',views.course_mcq,name='course_mcq'),
    re_path(r'^course_mcq_form$',views.course_mcq_form,name='course_mcq_form'),
    re_path(r'^coursemcq_form$',views.coursemcq_form,name='coursemcq_form'),
    re_path(r'^course_mcq_edit/(?P<mcqid>\d+)/$',views.course_mcq_edit,name='course_mcq_edit'),
    re_path(r'^course_mcq_update/(?P<mcqid>\d+)$',views.course_mcq_update,name='course_mcq_update'),
    re_path(r'^course_mcq_delete/(?P<mcqid>\d+)/$',views.course_mcq_delete,name='course_mcq_delete'),
    re_path(r'^tutorial_show$',views.tutorial_show,name='tutorial_show'),
    re_path(r'^tutorial_edit/(?P<tutorialid>\d+)/$',views.tutorial_edit,name='tutorial_edit'),
    re_path(r'^tutorial_update/(?P<tutorialid>\d+)$',views.tutorial_update,name='tutorial_update'),
    re_path(r'^tutorial_delete/(?P<tutorialid>\d+)/$',views.tutorial_delete,name='tutorial_delete'),
]
    
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
