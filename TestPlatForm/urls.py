"""TestPlantForm URL Configuration

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

from indexMod import urls as indexurls
from reportMod import urls as reporturls
from uiATMod import urls as uiATurls
from apiATMod import urls as apiATurls

urlpatterns = [
    path('', include(indexurls)),
    path('report-ind/', include(reporturls)),
    path('apiAT-ind/', include(apiATurls)),
    path('uiAT-ind/', include(uiATurls)),
    # path('', include(uiATurls)),
]
