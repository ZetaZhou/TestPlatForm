"""TestPlatForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
# from django.contrib import admin
from django.urls import path
from django.conf import urls
from uiATMod import views

urlpatterns = [
    path('', views.uiAT_index, name='uiAT_index'),
    path('uiAT_result/', views.uiAT_result, name='uiAT_result'),
    path('init-filetree/', views.init_filetree, name='init_filetree'),
    path('init_casetable/', views.init_casetable, name='init_casetable'),
    path('page_func/', views.page_func, name='page_func'),
    path('bkp_teststatus/', views.bkp_teststatus, name='bkp_teststatus'),
    path('run_case/', views.run_case, name='run_case'),
    path('info_loop/', views.info_loop, name='info_loop'),
    path('runloop_ctrl/', views.runloop_ctrl, name='runloop_ctrl'),
    path('result_download/', views.result_download, name='result_download'),
    path('send_resultmail/', views.send_resultmail, name='send_resultmail')
]
